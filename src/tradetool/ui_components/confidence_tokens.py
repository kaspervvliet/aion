
import streamlit as st

def show_confidence_level(level):
    if level == "low":
        st.markdown("🔘 **Confidence: Laag**", unsafe_allow_html=True)
    elif level == "medium":
        st.markdown("🟡 **Confidence: Gemiddeld**", unsafe_allow_html=True)
    elif level == "high":
        st.markdown("🟢 **Confidence: Hoog 🔥**", unsafe_allow_html=True)
    else:
        st.markdown("⚪ **Confidence: Onbekend**", unsafe_allow_html=True)
