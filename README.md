# selenium-automation-framework

## Project Overview
This project is a Selenium-based automation testing framework built using Python and PyTest. It follows the Page Object Model (POM) design pattern and demonstrates real-world QA automation practices.


## Tech Stack
- Python
- Selenium WebDriver
- PyTest
- WebDriver Manager

## Project Structure
selenium-framework/
│
├── pages/ # Page Object Models
├── tests/ # Test cases
├── reports/ # Test reports (generated)
├── conftest.py # Fixtures & setup
├── pytest.ini # Pytest configuration
└── requirements.txt


## Features
Page Object Model (POM) implementation  
Explicit waits using WebDriverWait  
Positive & negative test scenarios  
Screenshot capture on test failure  
HTML test reports  
Clean and scalable structure  


## Test Scenarios
-  Valid Login  
-  Invalid Login  
-  Error message validation  

## Test Execution Report

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/57653491-abb3-4c9a-a7c9-ce5ce4ccca36" />



## How to Run

```bash
pip install -r requirements.txt
pytest
