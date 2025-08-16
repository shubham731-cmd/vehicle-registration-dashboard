import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

def create_manufacturer_analysis(filters):
    st.header("🏭 Manufacturer Analysis")
    conn = sqlite3.connect("data/database/vehicle_data.db")
    query = """
    SELECT manufacturer, SUM(count) as total
    FROM vehicle_registrations
    WHERE strftime('%Y', registration_date) BETWEEN ? AND ?
    GROUP BY manufacturer
    """
    df = pd.read_sql_query(query, conn, params=(str(filters["start_year"]), str(filters["end_year"])))
    conn.close()

    if filters["manufacturers"]:
        df = df[df["manufacturer"].isin(filters["manufacturers"])]

    fig = px.pie(df, values="total", names="manufacturer", title="Market Share by Manufacturer")
    st.plotly_chart(fig, use_container_width=True)
