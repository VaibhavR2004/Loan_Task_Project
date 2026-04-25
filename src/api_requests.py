import requests
import csv

from .utils import create_json

URL = "https://jsonplaceholder.typicode.com/users"

HEADERS = {
    "User-Agent": "LoanReviewSystem",
    "Accept": "application/json"
}


def fetch_users():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=5)

        if response.status_code == 200:
            return response.json()
        else:
            print("Error:", response.status_code)
            return []

    except requests.exceptions.Timeout:
        print("Timeout error")
    except requests.exceptions.ConnectionError:
        print("Connection error")

    return []


def save_users_csv(users):
    data = []

    for u in users:
        data.append({
            "Name": u["name"],
            "Email": u["email"],
            "Company": u["company"]["name"],
            "City": u["address"]["city"]
        })

    with open("data/api_users.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    return data


def compare_with_loans(users_data):
    result = []

    for u in users_data:
        result.append({
            **u,
            "Potential_Relationship": False
        })

    create_json("data/customer_relation_report.json", result)


if __name__ == "__main__":
    users = fetch_users()
    parsed = save_users_csv(users)
    compare_with_loans(parsed)
