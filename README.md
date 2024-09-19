# Automated Testing of Social Media Platforms

This project provides an automated testing framework for social media platforms using Selenium WebDriver and Python.

## Features

- Automated browser setup using ChromeDriver
- Base test class for common setup and teardown operations
- Logging functionality for better debugging
- Support for multiple social media platforms

## Requirements

- Python 3.11+
- Selenium WebDriver
- ChromeDriver (automatically managed by WebDriverManager)
- pytest

## Installation

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Usage

Run tests using pytest:

`pytest src/test_social_media.py`


## Project Structure

- `src/base_test.py`: Contains the BaseTest class with common setup and teardown methods
- `src/test_social_media.py`: Implements specific test cases for social media platforms

