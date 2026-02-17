import streamlit as st
import pandas as pd
import time
from datetime import datetime

# --- SİSTEM AYARLARI ---
st.set_page_config(page_title="ASU Pinnacle Elite | Kayra", page_icon="🔱", layout="wide")

# --- ULTRA-PREMIUM ASU UI (CSS) ---
st.markdown("""
    <style>
    .stApp { 
        background: linear-gradient(135deg, #0f0f0f 0%, #2b030f 100%); 
        color: #f5f5f5; 
    }
    
    .main-title { 
        background: linear-gradient(90deg, #FFC627, #fdf5e6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Segoe UI', Roboto, sans-serif;
        font-size: 55px;
        font-weight: 900;
        text-align: center;
        margin-bottom: 0px;
    }

    .module-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 198, 39, 0.2);
        margin-bottom: 25px;
    }

    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #8C1D40 30%, #FFC627 90%);
        border: none;
        color: white !important;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px;
        transition: 0.4s;
    }
    .stButton>button:hover {
        box-shadow: 0 0 20px rgba(255, 198, 39, 0.6);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🔱 ASU PINNACLE ELITE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#FFC627; letter-spacing:5px; opacity:0.8; font-weight:bold;'>FULTON ENGINEERING ECOSYSTEM • V3.1</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚀 STRATEGY", "📅 MISSION CONTROL", "📊 ANALYTICS"])

# --- 1. MODÜL: ADMISSION STRATEGY (TAM LİSTE GERİ GELDİ!) ---
with tab1:
    st.subheader("Admission Probability Engine")
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.markdown("<div class='module-card'>", unsafe_allow_html=True)
        gpa = st.slider("Cumulative GPA", 2.0, 4.0, 3.8)
        sat = st.number_input("SAT Reasoning Score", 400, 1600, 1450)
        
        # TÜM PROJELER EKSİKSİZ GERİ EKLENDİ
        extra = st.multiselect("Innovation Portfolio", [
            "Robotics Club (Leadership)", 
            "Coding Bootcamp / Certifications", 
            "ASU Summer Engineering Program", 
            "Math / Science Olympiads", 
            "Sustainability Project (Green Tech)",
            "Open Source Contribution (GitHub)",
            "Entrepreneurial Venture (Startup)",
            "Volunteer Work / Community Service"
        ])
        
        if st.button("EXECUTE ANALYSIS"):
            with st.spinner("AI Evaluating Admission Tiers..."):
                time.sleep(1)
                # Hassas Algoritma
                score = max(min(int((gpa/4)*55 + (sat/1600)*30 + len(extra)*4), 98), 5)
                st.metric("Acceptance Probability", f"%{score}")
                if score > 85: st.balloons()
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_b:
        st.markdown("<div class='module-card'>", unsafe_allow_html=True)
        st.write("### 🧠 Admission Insights")
        st.info("ASU Fulton looks for innovation. Projects like 'Open Source' or 'Startup' increase your chances for specific scholarships.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 2. MODÜL: MISSION CONTROL (TAKTAK SİLME ÖZELLİĞİ) ---
with tab2:
    st.subheader("Real-Time Weekly Matrix")
    if 'my_courses' not in st.session_state or not all('id' in c for c in st.session_state.my_courses):
        st.session_state.my_courses = [{"id": 1, "Code": "CSE 110", "Day": "Monday", "Time": "10:30", "Loc": "BYENG 210"}]

    c_in, c_list = st.columns([1, 1])
    with c_in:
        st.markdown("<div class='module-card'>", unsafe_allow_html=True)
        with st.form("add_course"):
            f_code = st.text_input("Course Code", "CSE 120")
            f_loc = st.text_input("Room/Bldg", "GWC 487")
            f_day = st.selectbox("Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
            f_time = st.selectbox("Slot", ["09:00", "10:30", "12:00", "13:30", "15:00", "16:30"])
            if st.form_submit_button("DEPLOY"):
                st.session_state.my_courses.append({"id": int(time.time()*1000), "Code": f_code, "Day": f_day, "Time": f_time, "Loc": f_loc})
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with c_list:
        st.markdown("<div class='module-card' style='max-height: 400px; overflow-y: auto;'>", unsafe_allow_html=True)
        st.write("### 📋 Active Courses")
        for c in list(st.session_state.my_courses):
            sc1, sc2 = st.columns([4, 1])
            sc1.write(f"🔹 **{c['Code']}** | {c['Loc']}")
            if sc2.button("❌", key=f"del_{c['id']}"):
                st.session_state.my_courses = [item for item in st.session_state.my_courses if item['id'] != c['id']]
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    days, times = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], ["09:00", "10:30", "12:00", "13:30", "15:00", "16:30"]
    grid_df = pd.DataFrame({d: ["" for _ in times] for d in days}, index=times)
    for c in st.session_state.my_courses:
        if c['Day'] in days and c['Time'] in times:
            grid_df.at[c['Time'], c['Day']] = f"{c['Code']} @ {c['Loc']}"
    
    st.table(grid_df.style.map(lambda x: 'background-color: #8C1D40; color: #FFC627; font-weight: bold;' if x != "" else ""))

# --- 3. MODÜL: ANALYTICS (BURS VE FİNANS) ---
with tab3:
    st.subheader("Financial Intelligence")
    st.markdown("<div class='module-card'>", unsafe_allow_html=True)
    scholar = st.slider("Estimated Scholarship ($)", 0, 30000, 15000)
    net_val = 45774 - scholar
    ex_rate = 31.50 # Simulated Rate
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Annual Tuition", "$45,774")
    c2.metric("Merit Aid", f"-${scholar:,}")
    c3.metric("Net USD", f"${net_val:,}")
    
    st.write(f"### 🇹🇷 Current Estimated Cost: **{int(net_val * ex_rate):,} TRY**")
    st.bar_chart({"Scholarship": scholar, "Your Cost": net_val})
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; opacity:0.6; font-size:12px;'>KAYRA ENGINEERING PORTAL v3.1 | ARIZONA STATE UNIVERSITY</p>", unsafe_allow_html=True)