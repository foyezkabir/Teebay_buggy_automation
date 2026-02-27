"""
Playwright Smart Reporter
=========================
A custom pytest plugin that generates:
  1. A rich HTML executive-summary report (reports/summary.html)
  2. A Markdown bug report document (reports/bug_report.md)

Run via conftest.py or as a pytest plugin (listed in pytest.ini or conftest).
"""
from __future__ import annotations

import datetime
import json
import os
from pathlib import Path
from typing import Any

import pytest


REPORTS_DIR = Path(__file__).parent / "reports"


# ─────────────────────────────────────────────────────────────────────────────
# Plugin class
# ─────────────────────────────────────────────────────────────────────────────

class SmartReporter:
    """Collects test results and writes reports after the session ends."""

    def __init__(self):
        self.results: list[dict[str, Any]] = []
        self.start_time = datetime.datetime.now()

    # ── pytest hooks ──────────────────────────────────────────────────────

    def pytest_runtest_logreport(self, report: pytest.TestReport):
        if report.when == "call" or (report.when == "setup" and report.failed):
            outcome = "PASSED" if report.passed else ("FAILED" if report.failed else "SKIPPED")
            markers = [m.name for m in report.keywords.get("_markers", {}).values()
                       if hasattr(m, "name")] if hasattr(report, "keywords") else []

            self.results.append({
                "node_id": report.nodeid,
                "outcome": outcome,
                "duration": round(report.duration, 3),
                "longrepr": str(report.longrepr) if report.longrepr else "",
                "markers": markers,
                "module": report.nodeid.split("::")[0].replace("tests/", "").replace(".py", ""),
                "test_name": report.nodeid.split("::")[-1],
            })

    def pytest_sessionfinish(self, session: pytest.Session, exitstatus: int):
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        self._write_html_report()
        self._write_bug_report_md()

    # ── HTML report ───────────────────────────────────────────────────────

    def _write_html_report(self):
        end_time = datetime.datetime.now()
        total = len(self.results)
        passed = sum(1 for r in self.results if r["outcome"] == "PASSED")
        failed = sum(1 for r in self.results if r["outcome"] == "FAILED")
        skipped = sum(1 for r in self.results if r["outcome"] == "SKIPPED")
        duration = (end_time - self.start_time).total_seconds()

        # Group by module
        modules: dict[str, list] = {}
        for r in self.results:
            modules.setdefault(r["module"], []).append(r)

        pass_pct = round(passed / total * 100) if total else 0

        rows = ""
        for r in self.results:
            badge_class = {"PASSED": "pass", "FAILED": "fail", "SKIPPED": "skip"}.get(r["outcome"], "skip")
            error_html = ""
            if r["longrepr"]:
                short = r["longrepr"][:400].replace("<", "&lt;").replace(">", "&gt;")
                error_html = f'<details><summary>Details</summary><pre>{short}</pre></details>'
            rows += (
                f'<tr class="{badge_class.lower()}-row">'
                f'<td>{r["module"]}</td>'
                f'<td class="test-name">{r["test_name"].replace("_", " ")}</td>'
                f'<td><span class="badge {badge_class}">{r["outcome"]}</span></td>'
                f'<td>{r["duration"]}s</td>'
                f'<td>{error_html}</td>'
                f'</tr>'
            )

        module_summary = ""
        for mod, tests in modules.items():
            mp = sum(1 for t in tests if t["outcome"] == "PASSED")
            mf = sum(1 for t in tests if t["outcome"] == "FAILED")
            pct = round(mp / len(tests) * 100) if tests else 0
            module_summary += (
                f'<div class="module-card">'
                f'<h3>{mod.replace("test_", "").replace("_", " ").title()}</h3>'
                f'<div class="module-stats">'
                f'<span class="badge pass">{mp} Passed</span> '
                f'<span class="badge fail">{mf} Failed</span>'
                f'</div>'
                f'<div class="progress-bar"><div class="progress-fill" style="width:{pct}%"></div></div>'
                f'<small>{pct}% pass rate</small>'
                f'</div>'
            )

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Teebay-Buggy – Automation Test Report</title>
  <style>
    :root {{
      --pass: #22c55e; --fail: #ef4444; --skip: #f59e0b;
      --bg: #0f172a; --card: #1e293b; --text: #e2e8f0; --muted: #94a3b8;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: 'Segoe UI', sans-serif; background: var(--bg); color: var(--text); padding: 2rem; }}
    h1 {{ font-size: 1.8rem; margin-bottom: 0.5rem; }}
    .subtitle {{ color: var(--muted); margin-bottom: 2rem; }}
    .kpi-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin-bottom: 2rem; }}
    .kpi {{ background: var(--card); border-radius: 12px; padding: 1.5rem; text-align: center; }}
    .kpi .value {{ font-size: 2.5rem; font-weight: 700; }}
    .kpi .label {{ color: var(--muted); font-size: 0.85rem; margin-top: 0.25rem; }}
    .kpi.pass-kpi .value {{ color: var(--pass); }}
    .kpi.fail-kpi .value {{ color: var(--fail); }}
    .kpi.skip-kpi .value {{ color: var(--skip); }}
    .section-title {{ font-size: 1.2rem; margin: 2rem 0 1rem; border-left: 4px solid var(--pass); padding-left: 0.75rem; }}
    .modules {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1rem; margin-bottom: 2rem; }}
    .module-card {{ background: var(--card); border-radius: 10px; padding: 1rem; }}
    .module-card h3 {{ font-size: 0.95rem; margin-bottom: 0.5rem; }}
    .module-stats {{ margin-bottom: 0.5rem; }}
    .progress-bar {{ height: 6px; background: #334155; border-radius: 3px; overflow: hidden; margin: 0.5rem 0; }}
    .progress-fill {{ height: 100%; background: var(--pass); border-radius: 3px; }}
    .badge {{ display: inline-block; padding: 0.15rem 0.6rem; border-radius: 999px; font-size: 0.75rem; font-weight: 600; }}
    .badge.pass {{ background: rgba(34,197,94,.2); color: var(--pass); }}
    .badge.fail {{ background: rgba(239,68,68,.2); color: var(--fail); }}
    .badge.skip {{ background: rgba(245,158,11,.2); color: var(--skip); }}
    table {{ width: 100%; border-collapse: collapse; background: var(--card); border-radius: 12px; overflow: hidden; }}
    th {{ background: #0f172a; padding: 0.75rem 1rem; text-align: left; font-size: 0.8rem; color: var(--muted); text-transform: uppercase; }}
    td {{ padding: 0.65rem 1rem; border-bottom: 1px solid #1e293b; font-size: 0.85rem; vertical-align: top; }}
    .test-name {{ font-family: monospace; font-size: 0.8rem; }}
    .pass-row {{ border-left: 3px solid var(--pass); }}
    .fail-row {{ border-left: 3px solid var(--fail); background: rgba(239,68,68,0.04); }}
    .skip-row {{ border-left: 3px solid var(--skip); }}
    details summary {{ cursor: pointer; color: var(--fail); font-size: 0.8rem; }}
    details pre {{ background: #0f172a; border-radius: 6px; padding: 0.5rem; margin-top: 0.5rem; font-size: 0.73rem; white-space: pre-wrap; color: #f87171; }}
    footer {{ margin-top: 3rem; color: var(--muted); font-size: 0.8rem; text-align: center; }}
  </style>
</head>
<body>
  <h1>🤖 Teebay-Buggy Automation Report</h1>
  <p class="subtitle">Generated: {end_time.strftime("%Y-%m-%d %H:%M:%S")} &nbsp;|&nbsp; Duration: {duration:.1f}s</p>

  <div class="kpi-grid">
    <div class="kpi"><div class="value">{total}</div><div class="label">Total Tests</div></div>
    <div class="kpi pass-kpi"><div class="value">{passed}</div><div class="label">Passed</div></div>
    <div class="kpi fail-kpi"><div class="value">{failed}</div><div class="label">Failed</div></div>
    <div class="kpi skip-kpi"><div class="value">{pass_pct}%</div><div class="label">Pass Rate</div></div>
  </div>

  <div class="section-title">Module Breakdown</div>
  <div class="modules">{module_summary}</div>

  <div class="section-title">All Tests</div>
  <table>
    <thead><tr><th>Module</th><th>Test</th><th>Status</th><th>Duration</th><th>Error</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>

  <footer>Playwright + pytest | Teebay-Buggy QA Assessment</footer>
</body>
</html>"""

        report_path = REPORTS_DIR / "summary.html"
        report_path.write_text(html, encoding="utf-8")
        print(f"\n📊 Smart HTML report: {report_path}")

    # ── Bug report MD ─────────────────────────────────────────────────────

    def _write_bug_report_md(self):
        """Write a structured bug report for all FAILED tests."""
        failed_tests = [r for r in self.results if r["outcome"] == "FAILED"]

        lines = [
            "# Teebay-Buggy – Automated Bug Report",
            f"\n**Generated:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Total bugs detected:** {len(failed_tests)}\n",
            "---\n",
        ]

        for i, r in enumerate(failed_tests, 1):
            test_name = r["test_name"].replace("_", " ").strip()
            module = r["module"].replace("test_", "").replace("_", " ").title()
            short_repr = r["longrepr"][:600] if r["longrepr"] else "N/A"
            lines += [
                f"## Bug #{i}: {test_name}",
                f"- **Module:** {module}",
                f"- **Test ID:** `{r['node_id']}`",
                f"- **Severity:** To be assessed",
                f"- **Error:**\n```\n{short_repr}\n```",
                "",
            ]

        md_path = REPORTS_DIR / "automated_bug_report.md"
        md_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"🐛 Automated bug report: {md_path}")


# ─────────────────────────────────────────────────────────────────────────────
# Registration
# ─────────────────────────────────────────────────────────────────────────────

def pytest_configure(config: pytest.Config):
    config.pluginmanager.register(SmartReporter(), "smart_reporter")
