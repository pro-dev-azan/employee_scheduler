# Employee Scheduling Validation System

## Overview

This project is a Python based rule based system for managing and validating a simplified employee scheduling system. The system ensures that employee schedules comply with a set of predefined rules, and generrates a validation report listing any violations.

## Features

- **Rule Validation**: Validates schedules against multiple business rules.
- **Modular Design**: Uses object oriented programming and design patterns.
- **Report Generation**: Automatically generates a report listing any rule violations.

## How It Works

The code is organized into several key components, each handling a specific part of the validation process:

1. **`main.py`**: 
   - The entry point of the application.
   - Initializes the `ScheduleFacade`, which manages the overall process.
   - Loads the schedule data from `schedules.csv`.
   - Uses the `Validator` to check the data against various rules.
   - Generates a validation report (`validation_report.txt`).

2. **`facade.py`**:
   - Contains the `ScheduleFacade` class.
   - Provides a simplified interface to load data, validate it, and generate reports.
   - Coordinates between the `Validator` and the rule classes.

3. **`validator.py`**:
   - Contains the `Validator` class.
   - Manages a collection of rules and applies them to the schedule data.
   - Adds rules to the validator and validates the data accordingly.

4. **`rules/` Directory**:
   - Contains individual rule classes, each implementing a specific validation rule.
   - Examples include:
     - `one_shift_per_day_rule.py`: Ensures employees work only one shift per day.
     - `max_five_days_per_week_rule.py`: Ensures employees do not work more than 5 days a week.
     - `no_consecutive_night_shifts_rule.py`: Prevents consecutive night shifts for employees.
     - `consistent_name_rule.py`: Ensures consistency of employee names for the same `EmployeeID`.

5. **`tests/` Directory**:
   - Contains unit tests for the `ScheduleFacade`, `Validator`, and individual rule classes.
   - Ensures that each component and rule works as expected.

## Installation

1. Clone the back-end repository.
```bash
git clone https://github.com/pro-dev-azan/employee_scheduler.git
``` 
2. Install requirements
```bash
pip install -r requirements.txt
``` 
3. Change directory
```bash
cd employee_scheduler
``` 

## Usage
1. Prepare your schedules.csv file with the following columns:

    - EmployeeID (integer)
    - Name (string)
    - Day (string, e.g., "Monday", "Tuesday")
    - Shift (string, e.g., "Morning", "Afternoon", "Night")
2. Run the validation script:
```bash
python main.py
```
3. Check the validation_report.txt file for any rule violations.

## Running Tests
```bash
python -m unittest discover -s tests
```

This README.md provides the necessary information needed to set up and run your project without any unnecessary details.
