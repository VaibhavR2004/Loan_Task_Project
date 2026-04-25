import os
import unittest
import csv
from utils import load_json

DATA_PATH = "data/hdfc_loan_sample_20_rows.json"


class TestJSONCSV(unittest.TestCase):

    def test_json_file_exists(self):
        self.assertTrue(os.path.exists(DATA_PATH))

    def test_json_load(self):
        data = load_json(DATA_PATH)
        self.assertIsInstance(data, list)

    def test_record_count(self):
        data = load_json(DATA_PATH)
        self.assertEqual(len(data), 20)

    def test_csv_created(self):
        self.assertTrue(os.path.exists("data/processed_loans.csv"))

    def test_csv_columns(self):
        with open("data/processed_loans.csv", "r") as f:
            reader = csv.DictReader(f)
            columns = reader.fieldnames

        expected = [
            "Loan_ID", "Customer_Name", "Loan_Amount",
            "CIBIL_Score", "Loan_Status", "High_Risk_Flag"
        ]

        for col in expected:
            self.assertIn(col, columns)

    def test_csv_record_count(self):
        json_data = load_json(DATA_PATH)

        with open("data/processed_loans.csv", "r") as f:
            reader = list(csv.DictReader(f))

        self.assertEqual(len(reader), len(json_data))


if __name__ == "__main__":
    unittest.main()