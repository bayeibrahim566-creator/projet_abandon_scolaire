import streamlit as st
import requests

st.title("🎓 Prédiction du risque d'abandon scolaire")

url = "http://127.0.0.1:5000/predict"

# 🔥 TES 5 FEATURES EXACTES

average_grade = st.number_input("Note moyenne", 0.0, 20.0)
absenteeism_rate = st.number_input("Taux d'absentéisme", 0.0, 100.0)
study_time_hours = st.number_input("Temps d'étude (heures)", 0.0, 100.0)
study_absence_ratio = st.number_input("Ratio étude/absence", 0.0, 10.0)
score_global = st.number_input("Score global", 0.0, 20.0)

if st.button("Prédire"):

    data = {
        "average_grade": average_grade,
        "absenteeism_rate": absenteeism_rate,
        "study_time_hours": study_time_hours,
        "study_absence_ratio": study_absence_ratio,
        "score_global": score_global
    }

    response = requests.post(url, json=data)

    st.write("STATUS:", response.status_code)
    st.write("RESPONSE:", response.text)

    if response.status_code == 200:
        result = response.json().get("prediction")

        if result == 1:
            st.error("⚠️ Élève à risque d'abandon")
        else:
            st.success("✅ Élève non à risque")
    else:
        st.error("Erreur API")