# Teebay-Buggy  Playwright Automation Test Suite

End-to-end automation test suite for the **Teebay-Buggy** React application, built with **Python + Playwright + pytest** following the **Page Object Model (POM)** pattern.

This repository contains **both** the React application source and the automation test suite so that anyone can clone, run the app, and execute all tests with minimal setup.

---

## Repository Structure

```
(repo root)
 src/                        # React app source code
 public/                     # React app public assets
 package.json                # React app dependencies (yarn)
 yarn.lock

 tests/                      # pytest test modules (30 tests across 8 suites)
    test_login.py
    test_registration.py
    test_my_products.py
    test_add_product.py
    test_edit_product.py
    test_browse_products.py
    test_product_details.py
    test_account_settings.py

 pages/                      # Page Object classes (one per page)
 locators/                   # Element locator constants (one per page)
 auth/                       # Auth session helpers
 conftest.py                 # Root pytest fixtures (logged-in session, etc.)
 pytest.ini                  # pytest configuration
 requirements.txt            # Python dependencies
 smart_reporter.py           # Custom HTML + Markdown bug reporter plugin
 reports/                    # Auto-generated after each test run
     report.html             # pytest-html detailed report
     summary.html            # Executive KPI dashboard
     automated_bug_report.md # Bug list for all FAILED tests
```

---

## Prerequisites

| Requirement | Minimum version |
|---|---|
| Node.js | 18+ |
| yarn | 1.x |
| Python | 3.12+ |

---

## Quick Start

### Step 1  Clone the repository

```bash
git clone https://github.com/foyezkabir/Teebay_buggy_automation.git
cd Teebay_buggy_automation
```

---

### Step 2  Start the React application

```bash
# Install app dependencies
yarn install

# Start the dev server (keep this terminal open)
yarn start
```

The app will be available at **http://localhost:3000**. Wait until the browser (or terminal) confirms the app is running before proceeding to Step 3.

---

### Step 3  Set up the Python test environment

Open a **new terminal** in the same repo root:

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# macOS / Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Install Playwright's Chromium browser
playwright install chromium
```

---

### Step 4  Run the tests

```bash
# Run the full suite (30 tests)
pytest

# Run a specific test file
pytest tests/test_login.py -v

# Run a specific test by name
pytest tests/test_login.py::TestLoginHappyPath::test_successful_login -v

# Stop at the first failure
pytest -x

# Run with visible browser (useful for debugging)
pytest --headed
```

---

### Step 5  View reports

After any test run, reports are written to `reports/`:

| File | Description |
|---|---|
| `reports/report.html` | Detailed pytest-html test report |
| `reports/summary.html` | Executive KPI dashboard (pass/fail counts, duration) |
| `reports/report.json` | Machine-readable JSON results |
| `reports/automated_bug_report.md` | Markdown bug list for all failing tests |

Open in your browser:

```bash
# Windows
start reports\summary.html

# macOS
open reports/summary.html

# Linux
xdg-open reports/summary.html
```

---

## Test Credentials

| Field | Value |
|---|---|
| Email | `testuser@teebay.com` |
| Password | `123456` |

These are pre-configured in `config.py`  no changes needed.

---

## Test Suite Summary

| Test file | Tests | Area |
|---|---|---|
| `test_login.py` | 4 | Sign in  happy & sad paths |
| `test_registration.py` | 3 | Registration form |
| `test_my_products.py` | 5 | My Products list & delete |
| `test_add_product.py` | 6 | Add Product form |
| `test_edit_product.py` | 4 | Edit Product form |
| `test_browse_products.py` | 4 | Browse & filter products |
| `test_product_details.py` | 8 | Buy / Rent flows & modals |
| `test_account_settings.py` | 2 | Account settings form |
| **Total** | **30** | |

All 30 tests pass against the current app build.

---

## Locator Strategy

Because the app's `<label>` elements lack `for` attributes, `get_by_label()` cannot locate inputs. The suite uses:

| Element type | Strategy |
|---|---|
| Form inputs | `page.locator('input[name="fieldname"]')` |
| Buttons | `page.get_by_role("button", name="...")` |
| Semantic UI dropdowns | `page.get_by_role("listbox").nth(n)` |
| Text assertions | `page.get_by_text("...")` |
| Links | `page.get_by_role("link", name="...")` |
