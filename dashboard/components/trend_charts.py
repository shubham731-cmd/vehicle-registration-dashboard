import plotly.express as px
import streamlit as st
import sqlite3
import pandas as pd

def create_trend_analysis(filters):
    st.header("📊 Registration Trends")

    conn = sqlite3.connect("data/database/vehicle_data.db")
    query = """
    SELECT registration_date, vehicle_category, SUM(count) as total
    FROM vehicle_registrations
    WHERE strftime('%Y', registration_date) BETWEEN ? AND ?
    GROUP BY registration_date, vehicle_category
    """
    df = pd.read_sql_query(query, conn, params=(str(filters["start_year"]), str(filters["end_year"])))
    conn.close()

    if filters["categories"]:
        df = df[df["vehicle_category"].isin(filters["categories"])]

    fig = px.line(df, x="registration_date", y="total", color="vehicle_category", title="Monthly Registrations by Category")
    st.plotly_chart(fig, use_container_width=True)
