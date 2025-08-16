Vehicle Registration Dashboard:-
A Streamlit-based analytics dashboard for investor-grade insights from Indian vehicle registration data. Visualizes growth, trends, and manufacturer market share.

Features included:
1. Interactive dashboard with date range and category/manufacturer filters
2. YoY (Year-over-Year) and QoQ (Quarter-over-Quarter) growth analytics
3. Market share visualizations of top manufacturers
4. Fast, investor-friendly UI (Streamlit + Plotly)
5. Modular code and SQLite backend

Data Source & Assumptions:
  Primary Source:
1. Data schema and breakdowns match those available on Vahan Parivahan Dashboard as given in the assignment.

2. Intended for automated real-time scraping/ingestion from Vahan (using Selenium) but sample synthetic data is used for the default setup.

  Sample Data:
1. Generated via scripts/generate_sample_data.py
2. Includes years, months, vehicle categories (2W = two-wheeler, 3W = three-wheeler, 4W = four-wheeler), manufacturers, registration counts
3. Manufacturers and categories are representative of actual data on Vahan.

  Assumptions:

1. Vehicle categories: Only 2W, 3W, 4W are considered to focus on investor-relevant segments.
2. Manufacturer names: Most common Indian OEMs for each segment.
3. Data periodicity: Monthly across multiple years.

Setup Instructions
1. Clone Repository
    git clone https://github.com/yourusername/vehicle-registration-dashboard.git
    cd vehicle-registration-dashboard
2. Set Up Python Environment
    python -m venv venv
    Activate the environment:
    # Windows:
    venv\Scripts\activate
3. Install Dependencies
    pip install -r requirements.txt

4. Initialize Database & Insert Sample Data
    python scripts/setup_database.py
    python scripts/generate_sample_data.py
5. Run the Dashboard
    streamlit run dashboard/main.py

Open http://localhost:8501 to view the dashboard.

File Structure:
vehicle-registration-dashboard/
│
├── dashboard/
│   ├── main.py
│   ├── __init__.py
│   ├── assets/
│   └── components/
├── scripts/
│   ├── setup_database.py
│   ├── generate_sample_data.py
├── src/
│   └── database/
│       └── schema.sql
├── data/
│   └── database/
│       └── vehicle_data.db
├── requirements.txt
├── .env
└── README.md

BONUS-
Investment Insight:
1. Two-Wheeler Segment Continues to Dominate
2. Accelerating Shift Toward Electric Mobility
3. Four-Wheeler Growth—Market Share Shifts and Premiumization

