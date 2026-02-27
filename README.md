# Teebay-Buggy – Playwright Automation Test Suite

End-to-end automation test suite for the **Teebay-Buggy** React application.  
Built with **Python + Playwright + pytest** following the **Page Object Model (POM)** pattern.

---

## Project structure

```
automation_scripts/
├── conftest.py                 # Root pytest fixtures (logged-in session, etc.)
├── pytest.ini                  # pytest configuration (base_url, report options)
├── requirements.txt            # Python dependencies
├── smart_reporter.py           # Custom HTML + Markdown bug reporter plugin
│
├── locators/                   # Element locator constants (one file per page)
│   ├── login_locators.py
│   ├── register_locators.py
│   ├── my_products_locators.py
│   ├── add_product_locators.py
│   ├── edit_product_locators.py
│   ├── browse_products_locators.py
│   ├── product_details_locators.py
│   ├── account_settings_locators.py
│   └── navbar_locators.py
│
├── pages/                      # Page Object classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── register_page.py
│   ├── my_products_page.py
│   ├── add_product_page.py
│   ├── edit_product_page.py
│   ├── browse_products_page.py
│   ├── product_details_page.py
│   ├── account_settings_page.py
│   └── transactions_page.py
│
├── tests/                      # pytest test modules
│   ├── test_login.py           (7 tests)
│   ├── test_registration.py    (6 tests)
│   ├── test_my_products.py     (9 tests)
│   ├── test_add_product.py     (8 tests)
│   ├── test_edit_product.py    (8 tests)
│   ├── test_browse_products.py (10 tests)
│   ├── test_product_details.py (14 tests)
│   ├── test_account_settings.py(10 tests)
│   └── test_transactions.py   (4 tests)
│
└── reports/                    # Auto-generated (gitignored except .gitkeep)
    ├── report.html             # pytest-html report
    ├── report.json             # machine-readable JSON report
    ├── summary.html            # Smart Reporter – executive summary
    └── automated_bug_report.md # Smart Reporter – bug list for all FAILED tests
```

---

## Prerequisites

| Requirement | Version |
|---|---|
| Python | 3.12+ |
| Node.js | 18+ |
| yarn | 1.x |

---

## 1 – Start the application

```bash
# from the repo root (teebay-buggy/)
yarn install
yarn start
```

The app runs at **http://localhost:3000**.  
Keep this terminal open while running tests.

---

## 2 – Set up the Python environment

```bash
cd automation_scripts

# create a virtual environment
python -m venv venv

# activate it
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# macOS / Linux
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# install Playwright's Chromium browser
playwright install chromium
```

---

## 3 – Run the tests

```bash
# from automation_scripts/ with venv active

# run the full suite
pytest

# run a single test file
pytest tests/test_login.py

# run a specific test
pytest tests/test_login.py::test_successful_login

# run tests and stop at the first failure
pytest -x

# run with headed browser (useful for debugging)
pytest --headed
```

---

## 4 – View reports

After any test run, reports are written to `reports/`:

| File | Description |
|---|---|
| `reports/report.html` | Detailed pytest-html report |
| `reports/summary.html` | Smart Reporter – dark-themed KPI dashboard |
| `reports/report.json` | Machine-readable JSON results |
| `reports/automated_bug_report.md` | Markdown bug list for all failing tests |

Open the HTML reports directly in a browser:

```bash
start reports\summary.html          # Windows
open reports/summary.html           # macOS
xdg-open reports/summary.html       # Linux
```

---

## 5 – CI/CD (GitHub Actions)

The workflow file `.github/workflows/playwright-tests.yml` automatically:

1. Checks out the repo
2. Installs Node.js 18 + Yarn and starts the React app
3. Waits for `http://localhost:3000` to be ready
4. Sets up Python 3.12 and installs test dependencies
5. Installs Playwright Chromium with system dependencies
6. Runs the full pytest suite
7. Uploads HTML report, JSON report, executive summary, bug report, and failure screenshots as **GitHub Actions artifacts** (retained 30 days)

Triggers: pushes and pull requests to `main`/`master`, plus manual dispatch.

---

## 6 – Test credentials

| Field | Value |
|---|---|
| Email | `testuser@teebay.com` |
| Password | `123456` |

---

## 7 – Known bugs documented by the suite

| # | Area | Bug |
|---|---|---|
| 1 | Login | Password field type is `text` – password visible in plain text |
| 2 | Register | `firstName` field not validated (missing from yup schema) |
| 3 | Register | `confirmPassword` mismatch not validated |
| 4 | Register | Always shows server error on submit (backend not implemented) |
| 5 | My Products | Cricket kit and iPhone 13 appear **twice** (duplicate test data) |
| 6 | Transactions | `/transactions` renders My Products page content instead |
| 7 | Edit Product | Save button labelled **"Add Product"** (should be "Save" / "Update") |
| 8 | Edit Product | Selected categories not pre-filled in the multiselect dropdown |
| 9 | Add Product | Purchase Price / Rent Price labels missing on the Add form |
| 10 | Product Details | Rent modal "End date" label shows **"Last Name"** (copy-paste bug) |
| 11 | Product Details | User can **buy/rent their own product** (no ownership check) |
| 12 | Product Details | Rent allows **past start dates** |
| 13 | Product Details | Rent allows **end date before start date** |
| 14 | Account Settings | `phone_number` uses `yup.number()` but default value `"+123456789"` fails |
| 15 | Account Settings | No password change option available |

---

## 8 – Locator strategy

Because the app's `<label>` elements lack `for` attributes (confirmed via DOM inspection),
`get_by_label()` cannot locate form inputs.  The suite uses:

| Element type | Strategy |
|---|---|
| Form inputs | `page.locator('input[name="fieldname"]')` |
| Buttons | `page.get_by_role("button", name="...")` |
| Semantic UI dropdowns | `page.get_by_role("listbox").nth(n)` → click option |
| Text assertions | `page.get_by_text("...")` |
| Links | `page.get_by_role("link", name="...")` |
