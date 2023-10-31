# Automation Framework

This is a basic automation framework for testing a website https://demowebshop.tricentis.com/ 
using Selenium and the `unittest` testing framework in Python.

## Prerequisites

Before running the tests, make sure you have the following installed:

- Python
- Selenium WebDriver (`pip install selenium`)

## Running the Tests

To run the tests in Chrome Browser, follow these steps:
1. Navigate to the project directory:
`cd automation_webshop_draft`
2. Execute the test file:
` python tests_shop_examples.py` 
3. To run the tests in Firefox Browser, change browser 
(add # to comment Chrome and uncomment firefox:
#BROWSER = "chrome"
BROWSER = "firefox")

## Get new webdrivers

chromedriver https://googlechromelabs.github.io/chrome-for-testing/#stable
geckodriver https://github.com/mozilla/geckodriver/releases
