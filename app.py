import streamlit as st

def calculate_risk_score(age, diastolic_bp, troponin, qrs_duration, shortness_of_breath, history_vasovagal, no_hist_cardiac_disease, abnormal_ecg):
    score = 0

    if age >= 50:
        score += 1
    if diastolic_bp <= 50:
        score += 2
    if troponin > 99:
        score += 3
    if qrs_duration > 130:
        score += 2
    if shortness_of_breath:
        score += 1
    if history_vasovagal:
        score -= 1
    if no_hist_cardiac_disease:
        score -= 1
    if abnormal_ecg:
        score += 2

    return score

st.title("Canadian Syncope Risk Score Calculator")

st.write("Please provide patient details:")

age = st.number_input("Age:", min_value=0, max_value=120)
diastolic_bp = st.number_input("Diastolic Blood Pressure:", min_value=0, max_value=200)
troponin = st.number_input("Troponin level:", min_value=0, max_value=5000)
qrs_duration = st.number_input("QRS duration (ms):", min_value=0, max_value=500)

shortness_of_breath = st.checkbox("Shortness of breath?")
history_vasovagal = st.checkbox("History of vasovagal syncope?")
no_hist_cardiac_disease = st.checkbox("No history of cardiac disease?")
abnormal_ecg = st.checkbox("Abnormal ECG?")

if st.button("Calculate Risk Score"):
    score = calculate_risk_score(age, diastolic_bp, troponin, qrs_duration, shortness_of_breath, history_vasovagal, no_hist_cardiac_disease, abnormal_ecg)
    st.write(f"Canadian Syncope Risk Score: **{score}**")

st.write("Note: This app is for educational purposes only. Always consult with a medical professional before making clinical decisions.")
