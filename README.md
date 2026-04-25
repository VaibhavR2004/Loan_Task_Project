# Loan Review Task Project

## Project Overview

This project is developed for a task-based review of 3 engineers.

The objective is to evaluate practical backend development skills using:

- JSON Handling
- CSV Operations
- File Handling
- API Requests
- Data Parsing
- Error Handling
- Unit Testing
- Clean Code Structure

The project uses an HDFC Loan sample dataset containing 20 loan application records.

---

## Project Structure

loan_review_task/
│── data/
│   ├── hdfc_loan_sample_20_rows.json
│   ├── processed_loans.csv
│   ├── high_risk_loans.json
│   ├── loan_summary.txt
│   ├── api_users.csv
│   └── customer_relation_report.json
│
│── src/
│   ├── utils.py
│   ├── engineer_1_json_csv.py         Done by Vaibhav Kumar Rajput
│   ├── engineer_2_api_requests.py     Done by Shiva Chandra
│   └── engineer_3_unit_testing.py     Done by Anzar Ahmed
│
│── tests/
│   ├── test_json_csv.py
│   ├── test_api_requests.py
│   └── test_business_logic.py
│
│── requirements.txt
│── README.md

---

## Engineer 1 – JSON + CSV + File Handling

### Features

- Read loan dataset from JSON file
- Handle null / missing values
- Identify High Risk Customers using conditions:

### High Risk Conditions

- CIBIL Score < 650
- Credit History = 0
- Debt to Income Ratio > 0.6
- Default History Count > 0

If any 2 conditions match, customer is marked High Risk.

### Output Files

- processed_loans.csv
- high_risk_loans.json
- loan_summary.txt

---

## Engineer 2 – API Requests + Parsing

### Public API Used

https://jsonplaceholder.typicode.com/users

### Features

- GET Request using Python requests
- Custom Headers
- Parse JSON Response
- Extract:
  - Name
  - Email
  - Company
  - City

### Output Files

- api_users.csv
- customer_relation_report.json

### Error Handling

- Timeout Exception
- Connection Error
- Invalid Endpoint
- HTTP Errors

---

## Engineer 3 – Unit Testing

### Testing Includes

- JSON file validation
- High risk logic testing
- Boundary testing
- Null values testing
- API response testing
- Mock API testing using unittest.mock

### Run Tests

```bash
pytest -v
