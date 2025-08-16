import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import streamlit as st

from dashboard.components.kpi_section import create_kpi_section
from dashboard.components.trend_charts import create_trend_analysis
from dashboard.components.manufacturer_analysis import create_manufacturer_analysis
from dashboard.components.filters import create_sidebar_filters

def main():
    st.set_page_config(page_title="Vehicle Registration Analytics", page_icon="🚗", layout="wide")
    with open("dashboard/assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.title("🚗 Vehicle Registration Dashboard")
    st.markdown("Investor-focused insights for India's automotive sector")

    filters = create_sidebar_filters()

    create_kpi_section(filters)
    create_trend_analysis(filters)
    create_manufacturer_analysis(filters)

if __name__ == "__main__":
    main()
