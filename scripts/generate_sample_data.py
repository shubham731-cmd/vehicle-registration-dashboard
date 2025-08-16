import sqlite3
from datetime import datetime
import random

DB_PATH = "data/database/vehicle_data.db"

categories = ["2W", "3W", "4W"]
manufacturers = {
    "2W": ["Hero MotoCorp", "Honda", "TVS Motor", "Bajaj Auto"],
    "3W": ["Bajaj Auto", "Piaggio", "Mahindra", "TVS Motor"],
    "4W": ["Maruti Suzuki", "Hyundai", "Tata Motors", "Mahindra"]
}

def generate_data():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM vehicle_registrations;")
    cur.execute("DELETE FROM manufacturer_metrics;")

    for year in [2021, 2022, 2023, 2024]:
        for month in range(1, 13):
            for cat in categories:
                for manu in manufacturers[cat]:
                    count = random.randint(5000, 15000)
                    date = datetime(year, month, 1).strftime("%Y-%m-%d")
                    fy = f"FY{year}-{(year+1)%100}"
                    quarter = f"Q{((month - 1) // 3) + 1}"
                    cur.execute("""
                        INSERT INTO vehicle_registrations
                        (registration_date, vehicle_category, vehicle_class, manufacturer, state, rto_code, fuel_type, count, financial_year, quarter)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (date, cat, cat, manu, "PAN INDIA", "RTO001", "Petrol", count, fy, quarter))
    conn.commit()
    conn.close()
    print("Sample data inserted successfully ✅")

if __name__ == "__main__":
    generate_data()
