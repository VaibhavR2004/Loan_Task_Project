import csv

from .utils import load_json, create_json


def is_high_risk(record):
    conditions = 0

    cibil_score = record.get("CIBIL_Score") or 0
    credit_history = record.get("Credit_History") if record.get("Credit_History") is not None else 1
    debt_to_income = record.get("Debt_to_Income_Ratio") or 0
    default_count = record.get("Default_History_Count") or 0

    if cibil_score < 650:
        conditions += 1

    if credit_history == 0:
        conditions += 1

    if debt_to_income > 0.6:
        conditions += 1

    if default_count > 0:
        conditions += 1

    return conditions >= 2


def process_loans():
    data = load_json("data/hdfc_loan_sample_20_rows.json")

    if not data:
        print("No data found")
        return

    processed = []
    high_risk = []

    for record in data:
        risk = is_high_risk(record)

        processed.append({
            "Loan_ID": record["Loan_ID"],
            "Customer_Name": record["Customer_Name"],
            "Loan_Amount": record["Loan_Amount"],
            "CIBIL_Score": record["CIBIL_Score"],
            "Loan_Status": record["Loan_Status"],
            "High_Risk_Flag": risk
        })

        if risk:
            high_risk.append(record)

    with open("data/processed_loans.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=processed[0].keys())
        writer.writeheader()
        writer.writerows(processed)

    create_json("data/high_risk_loans.json", high_risk)

    approved = sum(1 for r in data if r["Loan_Status"] == "Approved")
    rejected = sum(1 for r in data if r["Loan_Status"] == "Rejected")

    with open("data/loan_summary.txt", "w") as file:
        file.write(f"Total Records: {len(data)}\n")
        file.write(f"Approved: {approved}\n")
        file.write(f"Rejected: {rejected}\n")
        file.write(f"High Risk: {len(high_risk)}\n")


def main():
    process_loans()


if __name__ == "__main__":
    main()
