# QA Test Case Generator

A Python-based QA automation utility that generates test cases from user-defined application features and exports them to multiple formats.

## Features

* Generate functional QA test cases automatically
* Support for multiple field types:

  * Text
  * Email
  * Password
  * Phone
  * Date
  * Checkbox
  * Radio Button
  * Dropdown
  * File Upload
  * Textarea
* Assign test case priorities (High, Medium, Low)
* Export to CSV
* Export to Excel (.xlsx)
* Generate Selenium automation test templates
* Save and load projects using JSON
* Excel Summary Dashboard
* Priority Distribution Pie Chart

---

## Technologies Used

* Python 3
* OpenPyXL
* Selenium
* JSON
* CSV
* Git
* GitHub

---

## Project Structure

```text
qa-test-generator/
│
├── main.py
├── test_generator.py
├── exporter.py
├── excel_exporter.py
├── selenium_exporter.py
├── project_manager.py
├── requirements.txt
├── README.md
│
├── output/
└── projects/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/hamertyme13/qa-test-generator.git
cd qa-test-generator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python main.py
```

---

## Example Usage

```text
Application Name: Banking App
Feature Name: Registration

Field Name: Username
Field Type: text

Field Name: Email
Field Type: email

Field Name: Password
Field Type: password
```

Generated outputs:

* CSV Report
* Excel Workbook
* Summary Dashboard
* Selenium Test Script

---

## Example Generated Test Cases

| Test ID | Scenario                         | Priority |
| ------- | -------------------------------- | -------- |
| TC001   | Registration with valid inputs   | High     |
| TC002   | Registration with empty Username | High     |
| TC003   | Registration with invalid Email  | Medium   |
| TC004   | Registration with weak Password  | Medium   |

---

## Selenium Script Generation

The application can generate Selenium automation templates automatically.

Example:

```python
def test_registration_with_empty_username(self):
    # Scenario: Registration with empty Username
    pass
```

---

## Skills Demonstrated

* Object-Oriented Programming (OOP)
* Test Design
* File Handling
* JSON Serialization
* Excel Reporting
* Data Visualization
* Automation Framework Concepts
* Git Version Control
* Software Documentation

---

## Future Enhancements

* Tkinter GUI
* API Test Case Generation
* PyTest Integration
* Selenium Page Object Model Support
* HTML Reporting
* TestRail Export
* Jira Integration

---

## Author

Joshua Hamer

GitHub: https://github.com/hamertyme13
LinkedIn: https://www.linkedin.com/in/joshua-hamer/
