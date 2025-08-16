import streamlit as st
import sqlite3
import pandas as pd

def get_unique_values(column):
    conn = sqlite3.connect("data/database/vehicle_data.db")
    values = pd.read_sql_query(f"SELECT DISTINCT {column} FROM vehicle_registrations", conn)[column].dropna().tolist()
    conn.close()
    return values

def create_sidebar_filters():
    st.sidebar.header("📊 Filters")
    start_year, end_year = st.sidebar.slider("Year Range", 2021, 2024, (2021, 2024))
    categories = st.sidebar.multiselect("Vehicle Categories", get_unique_values("vehicle_category"), default=["2W", "3W", "4W"])
    manufacturers = st.sidebar.multiselect("Manufacturer", get_unique_values("manufacturer"))

    return {
        "start_year": start_year,
        "end_year": end_year,
        "categories": categories,
        "manufacturers": manufacturers
    }
