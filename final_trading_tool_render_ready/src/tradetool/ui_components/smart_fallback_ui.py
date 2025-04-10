
import streamlit as st

def show_empty_state(message="Geen signalen vandaag.", hints=None):
    st.markdown(f"### 💤 {message}")
    if hints:
        st.markdown("#### 🔍 Hints:")
        for hint in hints:
            st.markdown(f"- {hint}")
