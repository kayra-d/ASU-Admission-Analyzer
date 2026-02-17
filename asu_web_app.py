import streamlit as st
import pandas as pd

# Sayfa tasarımı
st.set_page_config(page_title="ASU Master Portfolio", page_icon="🔱", layout="wide")

st.title("🔱 ASU Student Success & Planning Tool")
st.markdown("---")

# Menü Sekmeleri
tab1, tab2, tab3 = st.tabs(["📊 Profile Analyzer", "📅 Schedule Master", "💰 Tuition Tracker"])

with tab1:
    st.header("Admission Probability Analysis")
    gpa = st.slider("Select your GPA", 2.0, 4.0, 3.8)
    sat = st.number_input("SAT Score", 400, 1600, 1450)
    
    if st.button("Run Evaluation"):
        if gpa >= 3.5 and sat >= 1300:
            st.balloons()
            st.success("Strong candidate for ASU Engineering!")
        else:
            st.info("Good profile, but check individual course prerequisites.")

with tab2:
    st.header("Interactive Weekly Schedule")
    col1, col2 = st.columns(2)
    with col1:
        day = st.selectbox("Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
        course = st.text_input("Course Name (e.g. CSE 110)")
    with col2:
        start = st.time_input("Start Time")
        end = st.time_input("End Time")
    
    if st.button("Add Course"):
        st.write(f"✅ {course} added to {day}'s schedule logic.")

with tab3:
    st.header("Live Financial Tracker")
    st.metric(label="Annual Tuition", value="$45,774", delta="USD")
    st.info("Current Exchange Rate Integration: Active")