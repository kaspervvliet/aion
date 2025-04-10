
import sys
import os
import streamlit as st
from core.auto_mode_launcher import run_auto_mode
from core.strategy_config_loader import load_config
from core.gpt_validator import validate_strategy
from core.strategy_report_generator import generate_report
from core.streamlit_dashboard import launch_dashboard

st.set_page_config(page_title="Trading Tool Launcher", layout="wide")

st.title("🚀 Self-Learning Trading Tool – Main Launcher")

menu = st.sidebar.radio("Kies een actie", [
    "🔁 Auto Mode Analyse",
    "📊 Streamlit Dashboard",
    "📑 Strategie Rapport",
    "🤖 GPT Validatie",
])

config = load_config("core/strategy_config.json")

if menu == "🔁 Auto Mode Analyse":
    st.subheader("Auto Mode Strategie Analyse")
    run_auto_mode(config)

elif menu == "📊 Streamlit Dashboard":
    st.subheader("Visueel Dashboard")
    launch_dashboard(config)

elif menu == "📑 Strategie Rapport":
    st.subheader("Rapportage Genereren")
    report = generate_report(config)
    st.text(report)

elif menu == "🤖 GPT Validatie":
    st.subheader("Strategie Feedback van GPT")
    feedback = validate_strategy(config)
    st.markdown(f"**GPT Feedback:** {feedback}")
