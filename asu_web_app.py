import streamlit as st
import pandas as pd
import time
import requests
from datetime import datetime

# --- SİSTEM AYARLARI ---
st.set_page_config(page_title="ASU Pinnacle Elite | Kayra", page_icon="🔱", layout="wide")

# --- OTOMATİK KUR ÇEKME FONKSİYONU ---
def get_live_rate():
    try:
        # Ücretsiz ve hızlı bir API üzerinden anlık kur çekme
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD", timeout=5)
        return response.json()['rates']['TRY']
    except:
        return 34.50  # Bağlantı hatası durumunda yedek kur

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

# Yan menüde kur ayarı
live_usd_rate = get_live_rate()
with st.sidebar:
    st.title("⚙️ System Config")
    ex_rate = st.number_input("USD/TRY Exchange Rate (Live)", value=live_usd_rate, step=0.01)
    st.caption(f"Default rate fetched from Live API: {live_usd_rate}")

st.markdown("<h1 class='main-title'>🔱 ASU PINNACLE ELITE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#FFC627; letter-spacing:5px; opacity:0.8; font-weight:bold;'>FULTON ENGINEERING ECOSYSTEM • V3.5 FINAL</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚀 STRATEGY", "📅 MISSION CONTROL", "📊 ANALYTICS"])

# --- 1. MODÜL: ADMISSION STRATEGY ---
with tab1:
    st.subheader("Admission Probability & Statement Scanner")
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        st.markdown("<div class='module-card'>", unsafe_allow_html=True)
        gpa = st.slider("Cumulative GPA (Avg)", 2.0, 4.0, 2.4)
        sat = st.number_input("SAT Reasoning Score", 400, 1600, 1500)
        
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
        
        st.write("---")
        st.write("### 📝 Statement of Purpose Scanner")
        st.caption("Tip: Use keywords like 'resilience', 'transformation', and 'focus' to reflect your senior year turnaround.")
        essay = st.text_area("Analyze your essay for ASU Charter alignment...", placeholder="Paste your essay here...")
        
        if st.button("EXECUTE FULL ANALYSIS"):
            with st.spinner("AI Evaluating Admission Tiers..."):
                time.sleep(1.5)
                # Admission Algoritması (SAT & Transformation Ağırlıklı)
                base_score = (gpa/4)*40 + (sat/1600)*45 + len(extra)*4
                
                # Hikaye Analizi (Senin özel durumuna yönelik kelimeler eklendi)
                keywords = ["innovation", "impact", "inclusion", "resilience", "transformation", "focus", "potential", "growth"]
                match_count = sum(1 for word in keywords if word in essay.lower())
                essay_bonus = match_count * 3 # Essay bonusu artırıldı
                
                final_score = max(min(int(base_score + essay_bonus), 98), 5)
                
                st.metric("Acceptance Probability", f"%{final_score}")
                if sat >= 1450:
                    st.success("🔥 Elite SAT Score (1500+) detected. This acts as a 'Academic Competency' anchor.")
                if match_count >= 4:
                    st.info(f"✨ Powerful Narrative: Found {match_count} high-impact themes in your essay.")
                if final_score > 75: st.balloons()
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_b:
        st.markdown("<div class='module-card'>", unsafe_allow_html=True)
        st.write("### 🧠 Admission Insights")
        if sat >= 1500:
            st.info("Your SAT is in the top 1%. This proves that your 2.4 GPA was a temporary environmental setback, not an intellectual one.")
        st.warning("Strategy: Highlight the jump from 50s to 90 GPA in your senior year to trigger 'Holistic Review'.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 2. MODÜL: MISSION CONTROL ---
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

# --- 3. MODÜL: ANALYTICS (GELİŞTİRİLMİŞ NAMU BURS SİSTEMİ) ---
with tab3:
    st.subheader("Financial Intelligence & NAMU Predictor")
    st.markdown("<div class='module-card'>", unsafe_allow_html=True)
    
    # Otomatik Burs Hesaplayıcı (NAMU Matrix + Kayra Special Case)
    predicted_scholarship = 0
    if gpa >= 3.0:
        if gpa >= 3.9: predicted_scholarship = 15500
        elif gpa >= 3.7: predicted_scholarship = 10000
        elif gpa >= 3.3: predicted_scholarship = 5000
    elif sat >= 1500:
        # 1500 SAT ve 4. yıl başarısı ile zorlanacak burs miktarı
        predicted_scholarship = 11500 
        st.success("🎯 STRATEGIC WIN: Your 1500 SAT and high senior year GPA (90) make you a prime candidate for a NAMU Scholarship Appeal ($11,500+ expected).")
    
    st.write(f"### Current Analytics (GPA: {gpa} | SAT: {sat})")
    st.info(f"**Estimated Financial Aid: ${predicted_scholarship:,} / Year**")

    annual_tuition = 45774
    net_val = annual_tuition - predicted_scholarship
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Annual Tuition", f"${annual_tuition:,}")
    c2.metric("Estimated Aid", f"-${predicted_scholarship:,}")
    c3.metric("Net USD (Payable)", f"${net_val:,}")
    
    # TL Çevirisi (Anlık Kurla)
    total_try = int(net_val * ex_rate)
    st.write(f"### 🇹🇷 Total Cost: **{total_try:,} TRY** / Year")
    st.caption(f"Exchange Rate: 1 USD = {ex_rate} TRY (Adjustable in Sidebar)")
    
    chart_data = pd.DataFrame({
        'Category': ['Total Cost', 'After Aid'],
        'Amount': [annual_tuition, net_val]
    })
    st.bar_chart(data=chart_data, x='Category', y='Amount', color="#FFC627")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; opacity:0.6; font-size:12px;'>KAYRA ENGINEERING PORTAL v3.5 FINAL | ASU ELITE ADMISSION & SCHOLARSHIP ANALYZER</p>", unsafe_allow_html=True)