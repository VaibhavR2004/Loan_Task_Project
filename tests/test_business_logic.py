import unittest
from src.business_logic import is_high_risk


class TestBusinessLogic(unittest.TestCase):

    def test_high_risk_true(self):
        record = {
            "CIBIL_Score": 600,
            "Credit_History": 0,
            "Debt_to_Income_Ratio": 0.7,
            "Default_History_Count": 1
        }
        self.assertTrue(is_high_risk(record))

    def test_high_risk_false(self):
        record = {
            "CIBIL_Score": 750,
            "Credit_History": 1,
            "Debt_to_Income_Ratio": 0.3,
            "Default_History_Count": 0
        }
        self.assertFalse(is_high_risk(record))

    def test_null_values(self):
        record = {
            "CIBIL_Score": None,
            "Credit_History": None,
            "Debt_to_Income_Ratio": None,
            "Default_History_Count": None
        }
        result = is_high_risk(record)
        self.assertIsInstance(result, bool)

    def test_boundary_cibil(self):
        record = {
            "CIBIL_Score": 650,
            "Credit_History": 0,
            "Debt_to_Income_Ratio": 0.7,
            "Default_History_Count": 0
        }
        self.assertTrue(is_high_risk(record))


if __name__ == "__main__":
    unittest.main()