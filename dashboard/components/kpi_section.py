import streamlit as st
import sqlite3
import pandas as pd

def create_kpi_section(filters):
    st.header("📈 Key Performance Indicators")
    conn = sqlite3.connect("data/database/vehicle_data.db")
    query = """
    SELECT * FROM vehicle_registrations
    WHERE strftime('%Y', registration_date) BETWEEN ? AND ?
    """
    df = pd.read_sql_query(query, conn, params=(str(filters["start_year"]), str(filters["end_year"])))
    conn.close()

    if filters["categories"]:
        df = df[df["vehicle_category"].isin(filters["categories"])]
    if filters["manufacturers"]:
        df = df[df["manufacturer"].isin(filters["manufacturers"])]

    total_regs = df["count"].sum()
    yoy_growth = df.groupby("vehicle_category")["count"].sum().pct_change().mean() * 100 if not df.empty else 0
    market_leader = df.groupby("manufacturer")["count"].sum().sort_values(ascending=False).head(1)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Registrations", f"{total_regs:,}")
    col2.metric("Avg YoY Growth", f"{yoy_growth:.2f}%")
    if not market_leader.empty:
        col3.metric("Market Leader", f"{market_leader.index[0]}: {market_leader.iloc[0]}")
