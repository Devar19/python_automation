# Selenium Python Automation Framework

A scalable Selenium WebDriver automation framework developed in Python using PyTest, Unittest, Page Object Model (POM), configuration management, CSV-based test data, explicit waits, screenshot capture on failure, and HTML reporting.

---

## 1. Project Overview

This project demonstrates the development of a structured Selenium Python automation framework for testing an e-commerce web application.

The framework automates:

- User login
- Positive and negative login scenarios
- Product search
- Login-to-product-search integration flow

The framework is designed using reusable components so that test cases remain independent from Selenium implementation details.

---

## 2. Application Under Test

The framework uses the TutorialsNinja demo e-commerce application:

https://tutorialsninja.com/demo/

The application is used for demonstrating:

- Login automation
- Account-page validation
- Product search
- Integration testing

---

## 3. Objectives

The framework demonstrates the following automation concepts:

- Selenium WebDriver
- Python
- PyTest
- Unittest
- Page Object Model
- Reusable base-page methods
- Explicit waits
- Configuration management
- CSV-based test-data management
- Secure credential handling
- Browser/driver factory
- Screenshot capture on failure
- HTML test reporting
- Integration testing
- Parameterized testing
- Test markers
- Maintainable project structure

---

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Selenium WebDriver | Browser automation |
| PyTest | Main test framework |
| Unittest | Demonstration of Python's built-in testing framework |
| pytest-html | HTML test reporting |
| pytest-metadata | Metadata support for HTML reports |
| CSV | External test data |
| ConfigParser | Configuration management |
| Chrome WebDriver | Browser automation |

### Versions

- Python: 3.14.7
- Selenium: 4.49.0
- PyTest: 9.1.1
- pytest-html: 4.2.0
- pytest-metadata: 3.1.1

---

## 5. Framework Architecture

The framework follows a layered architecture:

```text
                    Test Execution
                          |
             +------------+------------+
             |                         |
           PyTest                  Unittest
             |                         |
             +------------+------------+
                          |
                          v
                    Test Layer
                          |
                          v
                 Page Object Layer
                          |
          +---------------+---------------+
          |               |               |
          v               v               v
      LoginPage      AccountPage     ProductPage
          |               |               |
          +---------------+---------------+
                          |
                          v
                       BasePage
                          |
                          v
                  Selenium WebDriver
                          |
                          v
                    Web Application
```

Supporting layers provide:

```text
Configuration
      |
      v
 ConfigReader

Test Data
      |
      v
  CSVReader

Credentials
      |
      v
CredentialReader

Browser Creation
      |
      v
 DriverFactory

Failure Handling
      |
      v
ScreenshotUtility
```

---

## 6. Project Structure

```text
Capstone_Project/
│
├── .gitignore
├── README.md
├── requirements.txt
├── pytest.ini
├── conftest.py
│
├── config/
│   └── config.ini
│
├── data/
│   ├── login_data.csv
│   └── product_data.csv
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── account_page.py
│   └── product_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_config.py
│   ├── test_csv_reader.py
│   ├── test_driver.py
│   ├── test_login_pytest.py
│   ├── test_login_unittest.py
│   ├── test_login_and_product_search.py
│   └── test_product_search_pytest.py
│
├── utils/
│   ├── __init__.py
│   ├── config_reader.py
│   ├── credentials.py
│   ├── csv_reader.py
│   ├── driver_factory.py
│   └── screenshot.py
│
└── reports/
    ├── report.html
    └── screenshots/
```

---

## 7. Page Object Model

The framework uses the Page Object Model design pattern.

Each important application page has a dedicated Python class.

### LoginPage

Responsible for:

- Opening the login page
- Entering email
- Entering password
- Clicking Login
- Reading login errors

### AccountPage

Responsible for:

- Validating successful login
- Detecting the Account page
- Navigating back to the Home page

### ProductPage

Responsible for:

- Entering product search terms
- Executing product searches
- Retrieving product names
- Verifying that a requested product is displayed

### BasePage

Provides common Selenium operations such as:

- Clicking elements
- JavaScript clicking
- Entering text
- Reading text
- Waiting for elements
- Checking element visibility

This avoids duplicating Selenium logic across individual Page Objects.

---

## 8. Configuration Management

Application and browser settings are stored outside the test code.

Example:

```ini
[application]
url = https://tutorialsninja.com/demo/

[browser]
name = chrome

[test]
timeout = 10
```

The `ConfigReader` class loads these values.

This allows settings such as the application URL, browser, and timeout to be changed without modifying individual tests.

---

## 9. Browser Driver Factory

`DriverFactory` centralizes browser creation.

Currently supported browsers include:

- Chrome
- Firefox

Example:

```python
driver = DriverFactory.create_driver(
    config.get_browser()
)
```

This prevents browser initialization code from being duplicated across tests.

---

## 10. Test Data Management

Login and product-search data are stored externally in CSV files.

### Login Data

```csv
email,password_type,expected_result
customertester@example.com,valid,success
customertester@example.com,invalid,failure
customertest1@example.com,invalid,failure
customertest1@example.com,invalid,failure
,invalid,failure
```

### Product Data

```csv
product
MacBook
MacBook Air
```

The `CSVReader` utility loads this data into Python dictionaries.

---

## 11. Credential Management

Actual passwords are not stored in the CSV file.

The valid test password is supplied through an environment variable:

```text
TN_TEST_PASSWORD
```

In PowerShell:

```powershell
$env:TN_TEST_PASSWORD="your_password"
```

Do not commit the password to the repository.

---

## 12. Explicit Waits

The framework uses Selenium's `WebDriverWait` and Expected Conditions rather than fixed delays.

Examples include:

```python
EC.element_to_be_clickable()
```

```python
EC.visibility_of_element_located()
```

```python
EC.presence_of_element_located()
```

This improves reliability when application elements take time to appear or become interactive.

---

## 13. Screenshot on Failure

The framework automatically captures screenshots when a PyTest test fails.

The screenshot mechanism is implemented through the:

```text
pytest_runtest_makereport
```

hook.

Screenshots are stored under:

```text
reports/screenshots/
```

This provides visual evidence for failed browser tests and helps with debugging.

---

## 14. HTML Reporting

The framework uses `pytest-html`.

Reports are generated automatically using the configuration in:

```text
pytest.ini
```

The report is:

```text
reports/report.html
```

The report contains test execution information and PyTest metadata.

---

## 15. Test Scenarios

### Login Tests

The framework covers:

1. Valid login
2. Invalid password
3. Invalid credentials
4. Invalid user
5. Blank email

The expected result is stored in the CSV test data.

---

### Product Search Tests

The framework tests:

- MacBook
- MacBook Air

The product search is parameterized using CSV test data.

---

### Integration Test

The integration test performs:

```text
Open application
      ↓
Open Login
      ↓
Login
      ↓
Verify Account page
      ↓
Return to Home
      ↓
Search product
      ↓
Verify product
```

---

## 16. PyTest

The framework uses PyTest for parameterized testing and test execution.

Example:

```python
@pytest.mark.parametrize(
    "data",
    test_data
)
def test_login(data, driver, config):
    ...
```

This allows multiple test scenarios to execute using the same test implementation.

---

## 17. Unittest

A separate Unittest implementation is included to demonstrate compatibility with Python's built-in testing framework.

Run it using:

```powershell
python -m unittest tests.test_login_unittest -v
```

---

## 18. PyTest Marker

Integration tests are marked with:

```python
@pytest.mark.integration
```

The marker is registered in `pytest.ini`.

Integration tests can therefore be selected separately:

```powershell
pytest -m integration
```

---

## 19. Installation

### Step 1: Clone or copy the project

Place the project in a local directory.

### Step 2: Create a virtual environment

```powershell
python -m venv .venv
```

### Step 3: Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

```powershell
pip install -r requirements.txt
```

### Step 5: Configure credentials

Set the environment variable:

```powershell
$env:TN_TEST_PASSWORD="your_password"
```

Do not commit the password to the repository.

---

## 20. Running the Tests

### Run the complete PyTest suite

```powershell
pytest -v
```

### Run login tests

```powershell
pytest -v tests/test_login_pytest.py
```

### Run product-search tests

```powershell
pytest -v tests/test_product_search_pytest.py
```

### Run integration tests

```powershell
pytest -v tests/test_login_and_product_search.py
```

### Run only integration-marked tests

```powershell
pytest -v -m integration
```

### Run Unittest

```powershell
python -m unittest tests.test_login_unittest -v
```

---

## 21. Reports

After PyTest execution:

```text
reports/
└── report.html
```

The report can be opened in a web browser.

When failures occur, screenshots are saved under:

```text
reports/screenshots/
```

---

## 22. Current Test Results

The current complete regression suite contains 13 tests.

Latest successful execution:

```text
13 passed in 82.42s
```

Test coverage includes:

- Configuration validation
- CSV reader validation
- Driver creation
- Login
- Negative login scenarios
- Unittest login
- Product search
- Login + product search integration

---

## 23. Design Benefits

The framework provides:

### Maintainability

Application locators are centralized inside Page Objects.

### Reusability

Common Selenium operations are implemented once in `BasePage`.

### Scalability

Additional pages and tests can be added without restructuring the entire framework.

### Reliability

Explicit waits reduce timing-related synchronization problems.

### Data-driven testing

CSV files allow multiple scenarios to execute using the same test logic.

### Security

Actual credentials are provided through environment variables rather than being stored directly in test data.

### Debugging

Automatic screenshots and HTML reports provide evidence when tests fail.

### Separation of concerns

Configuration, test data, credentials, browser creation, page interaction, and test assertions are maintained in separate components.

---

## 24. Future Improvements

Possible future enhancements include:

- Cross-browser execution
- Parallel test execution
- Logging framework
- Allure reporting
- CI/CD integration
- Docker-based execution
- Remote Selenium Grid
- API + UI hybrid testing
- Database validation
- Environment-specific configuration
- Secret management through CI/CD tools
- Retry mechanism for selected transient failures

---

## 25. Conclusion

This project demonstrates a structured Selenium Python automation framework rather than a collection of standalone Selenium scripts.

The framework combines:

- Selenium WebDriver
- PyTest
- Unittest
- Page Object Model
- Explicit waits
- Configuration management
- CSV test data
- Environment-based credentials
- Browser factory
- Screenshot capture
- HTML reporting
- Integration testing

The resulting architecture is designed to make automated tests easier to maintain, reuse, debug, and extend.
