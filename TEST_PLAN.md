# Teebay-Buggy — Test Plan

---

## 1. Application Overview

**Teebay-Buggy** is a React-based peer-to-peer marketplace where users can list, browse, buy, and rent products. It uses Redux for state management and React Router for navigation.

---

## 2. Scope

All end-to-end functional tests executed via **Python + Playwright + pytest** against a locally running dev server at `http://localhost:3000`.

---

## 3. Test Suites & Coverage

### 3.1 Authentication — `test_login.py` (4 tests)

| # | Test Case | Type |
|---|---|---|
| 1 | Render login page correctly | Happy |
| 2 | Successful login with valid credentials | Happy |
| 3 | Login fails with wrong password | Sad |
| 4 | Login fails with unregistered email | Sad |

**Credentials used:** `testuser@teebay.com` / `123456`

---

### 3.2 Registration — `test_registration.py` (3 tests)

| # | Test Case | Type |
|---|---|---|
| 1 | Registration page renders correctly | Happy |
| 2 | Successful new user registration | Happy |
| 3 | Registration fails with existing email | Sad |

---

### 3.3 My Products — `test_my_products.py` (5 tests)

| # | Test Case | Type |
|---|---|---|
| 1 | My Products page renders for logged-in user | Happy |
| 2 | Listed products are visible | Happy |
| 3 | Product card shows correct details | Happy |
| 4 | Delete product removes it from list | Happy |
| 5 | Empty state shown when no products exist | Edge |

---

### 3.4 Add Product — `test_add_product.py` (6 tests)

| # | Test Case | Type |
|---|---|---|
| 1 | Add Product form renders | Happy |
| 2 | Successfully submit a new product | Happy |
| 3 | Category multi-select works | Happy |
| 4 | Buy price field accepts valid input | Happy |
| 5 | Rent price + period fields accept valid input | Happy |
| 6 | Form validation blocks empty submission | Sad |

---

### 3.5 Edit Product — `test_edit_product.py` (4 tests)

| # | Test Case | Type |
|---|---|---|
| 1 | Edit form pre-populates with existing data | Happy |
| 2 | Successfully update product details | Happy |
| 3 | Successfully update price fields | Happy |
| 4 | Cancel edit navigates back without changes | Edge |

---

### 3.6 Browse Products — `test_browse_products.py` (4 tests)

| # | Test Case | Type |
|---|---|---|
| 1 | Browse page renders product listings | Happy |
| 2 | Products owned by current user are NOT shown | Logic |
| 3 | Product cards show title, category, price | Happy |
| 4 | Navigating to a product opens details page | Happy |

---

### 3.7 Product Details & Buy/Rent Visibility — `test_product_details.py` (8 tests)

This is the most critical suite covering the **buy/rent visible logic**.

**Buy/Rent Visibility Rule:**
> A logged-in user must **not** see Buy or Rent buttons on products they own. These actions are only available on products listed by *other* users.

| # | Test Case | Type |
|---|---|---|
| 1 | Product details page renders correctly | Happy |
| 2 | **Buy button visible for other user's product** | Logic |
| 3 | **Rent button visible for other user's product** | Logic |
| 4 | **Buy/Rent buttons NOT shown on own product** | Logic |
| 5 | Buy confirmation modal opens and confirms | Happy |
| 6 | Rent modal opens with date picker and confirms | Happy |
| 7 | Rent period selection works correctly | Happy |
| 8 | Closing modal cancels the action | Edge |

---

### 3.8 Account Settings — `test_account_settings.py` (2 tests)

| # | Test Case | Type |
|---|---|---|
| 1 | Account settings form renders with existing data | Happy |
| 2 | Successfully update account information | Happy |

---

## 4. Total Coverage

| Metric | Value |
|---|---|
| Total test cases | **30** |
| Happy path | 20 |
| Sad / negative path | 4 |
| Business logic / visibility | 4 |
| Edge cases | 2 |
| Test files | 8 |
| Browser | Chromium (Playwright) |

---

## 5. Out of Scope

- Admin functionality
- Payment/transaction processing (mocked)
- Mobile/responsive layout testing
- Cross-browser testing (Firefox, Safari)
- Performance / load testing
- API-level (unit/integration) testing

---

## 6. Pass Criteria

All 30 tests pass with exit code `0`. Reports generated at `automation_scripts/reports/report.html`.
