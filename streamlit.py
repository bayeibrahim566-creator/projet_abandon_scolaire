import streamlit as st
import joblib
import numpy as np

st.title("🎓 Prédiction du risque d'abandon scolaire")

# Charger le modèle
model = joblib.load("model_dropout.pkl")

# Inputs utilisateur
average_grade = st.number_input("Note moyenne", 0.0, 20.0)
absenteeism_rate = st.number_input("Taux d'absentéisme", 0.0, 100.0)
study_time_hours = st.number_input("Temps d'étude (heures)", 0.0, 100.0)
study_absence_ratio = st.number_input("Ratio étude/absence", 0.0, 10.0)
score_global = st.number_input("Score global", 0.0, 20.0)

if st.button("Prédire"):

    # Construire le vecteur d'entrée (IMPORTANT: ordre = entraînement modèle)
    X = np.array([[average_grade,
                   absenteeism_rate,
                   study_time_hours,
                   study_absence_ratio,
                   score_global]])

    # Prédiction
    prediction = model.predict(X)[0]

    # Résultat
    if prediction == 1:
        st.error("⚠️ Élève à risque d'abandon")
    else:
        st.success("✅ Élève non à risque")