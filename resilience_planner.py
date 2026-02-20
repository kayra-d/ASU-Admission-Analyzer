import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Resilience Study Planner", page_icon="🧠")

st.title("🧠 Resilience Study Planner")
st.markdown("---")

# Kullanıcı Girişi: Bugünün Odaklanma Verisi
with st.expander("📝 Log Today's Performance", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        study_hours = st.slider("Hours Studied", 0.0, 12.0, 4.0)
        focus_level = st.select_slider("Focus Intensity", options=["Low", "Medium", "High", "Elite"])
    with col2:
        environment = st.selectbox("Study Environment", ["Home", "Library", "Cafe", "School"])
        distractions = st.multiselect("Main Distractions", ["Social Media", "Noise", "Personal Stress", "Boredom"])

if st.button("SAVE DAILY DATA"):
    st.success("Data points saved. Resilience index updated!")
    # Burada veriyi kaydetme mantığı çalışacak

# ASU Özel: Growth Analytics
st.subheader("📈 Academic Transformation Roadmap")
# Örnek veri ile gelişim grafiği (Senin hikayeni temsil eden bir grafik)
growth_data = pd.DataFrame({
    'Month': ['Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
    'Focus Score': [45, 58, 72, 85, 92]
})
fig = px.line(growth_data, x='Month', y='Focus Score', title='Your Resilience Growth Curve')
st.plotly_chart(fig)
# --- RESILIENCE ALGORITHM (The "Kayra" Factor) ---
def calculate_resilience_score(hours, intensity, distraction_count):
    # Bu algoritma senin akademik dönüşüm mantığını simüle eder
    intensity_map = {"Low": 1, "Medium": 2, "High": 3, "Elite": 5}
    base = (hours * intensity_map[intensity])
    penalty = distraction_count * 1.5
    score = max(base - penalty, 0)
    return score

# --- UI GÜNCELLEMESİ ---
st.markdown("---")
st.subheader("🚀 Transformation Intelligence")

# Senin lise verilerini sisteme 'Golden Standard' olarak gömüyoruz
st.info("""
**Global Benchmark:** This system uses the 'Kayra Transformation' model 
(moving from a 50% baseline to a 90% performance index by optimizing 
environmental focus factors).
""")

# Hesaplama butonu altına ekle:
res_score = calculate_resilience_score(study_hours, focus_level, len(distractions))
st.metric("Your Resilience Score Today", f"{res_score:.1f} pts")

if res_score > 15:
    st.success("🔥 High Performance Detected: You are currently on track for a 'Senior Year Turnaround' (90+ GPA Pace).")
    # Sayfanın en altına veya sidebar'a eklenecek not
st.sidebar.markdown("---")
st.sidebar.info(f"""
**🎯 Project Purpose for ASU:**
This tool was engineered to model the academic resilience I demonstrated during my high school years. 
By quantifying focus variables, I transformed my performance from a **53% baseline to 90%**, 
matching my **1500 SAT** potential.
""")