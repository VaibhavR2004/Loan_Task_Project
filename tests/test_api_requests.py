import unittest
from src.engineer_2_requests import fetch_users

class TestAPI(unittest.TestCase):

    def test_api_fetch(self):
        data = fetch_users()

    
        self.assertTrue(len(data) > 0)

    
        self.assertIn("name", data[0])
        self.assertIn("email", data[0])
        self.assertIn("company", data[0])
        self.assertIn("address", data[0])


if __name__ == "__main__":
    unittest.main()