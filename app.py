import streamlit as st

# Title and introduction
st.title('Canadian Syncope Risk Score Calculator')
st.write('This tool calculates the risk of serious adverse events after syncope.')

# Creating a form for user input
with st.form('risk_score_form'):
    st.subheader('Clinical Evaluation')
    predisposition_to_vasovagal_symptoms = st.radio(
        'Predisposition to Vasovagal Symptoms:',
        options=['No', 'Yes'],
        index=0,  # Default to 'No'
        horizontal = True,
        help = "Triggered by being in a warm crowded place, prolonged standing, fear, emotion, or pain"
    )
    history_of_heart_disease = st.radio(
        'History of Heart Disease:',
        options=['No', 'Yes'],
        index=0,  # Default to 'No'
        horizontal = True,
        help = "CAD, atrial fibrillation or flutter, CHF, valvular disease"
        
    )
    systolic_bp_reading = st.radio(
        'Any Systolic Pressure Reading <90 or >180 mmHg:',
        options=['No', 'Yes'],
        index=0,  # Default to 'No'
        horizontal = True
    )

    st.subheader('Investigations')
    elevated_troponin_level = st.radio(
        'Elevated Troponin Level:',
        options=['No', 'Yes'],
        index=0,  # Default to 'No'
        horizontal = True
    )
    abnormal_qrs_axis = st.radio(
        'Abnormal QRS Axis:',
        options=['No', 'Yes'],
        index=0,  # Default to 'No'
        horizontal = True
    )
    qrs_duration = st.radio(
        'QRS Duration >130 ms:',
        options=['No', 'Yes'],
        index=0,  # Default to 'No'
        horizontal = True
    )
    corrected_qt_interval = st.radio(
        'Corrected QT Interval >480 ms:',
        options=['No', 'Yes'],
        index=0,  # Default to 'No'
        horizontal = True
    )
    diagnosis = st.radio(
        'Emergency Department Diagnosis:',
        options=['Vasovagal Syncope', 'Cardiac Syncope', 'Neither'],
        index=2,  # Default to 'Neither'
        horizontal = True
    )

    submit_button = st.form_submit_button('Calculate Risk Score')

# Logic for calculating the score
if submit_button:
    score = 0
    # Clinical evaluation
    score -= 1 if predisposition_to_vasovagal_symptoms == 'Yes' else 0
    score += 1 if history_of_heart_disease == 'Yes' else 0
    score += 2 if systolic_bp_reading == 'Yes' else 0

    # Investigations
    score += 2 if elevated_troponin_level == 'Yes' else 0
    score += 1 if abnormal_qrs_axis == 'Yes' else 0
    score += 1 if qrs_duration == 'Yes' else 0
    score += 2 if corrected_qt_interval == 'Yes' else 0

    # Diagnosis in emergency department
    if diagnosis == 'Vasovagal Syncope':
        score -= 2
    elif diagnosis == 'Cardiac Syncope':
        score += 2
    
    # Output results
    risk_category = ('Very Low' if score <= -2 else
                     'Low' if score <= 0 else
                     'Medium' if score <= 3 else
                     'High' if score <= 5 else
                     'Very High')
    st.write(f'Your Canadian Syncope Risk Score is: {score}')
    st.write(f'Estimated Risk Category: {risk_category}')

    estimated_risk_of_serious_adverse_events = {-3: 0.4, -2: 0.7, -1: 1.2, 0: 1.9, 1: 3.1, 2: 5.1, 3: 8.1, 4: 12.9, 5: 19.7, 6:28.9, 7:40.3, 8:52.8, 9:65.0, 10: 75.5, 11:83.6}
    st.write(f'Estimated Risk of Serious Adverse Events: {estimated_risk_of_serious_adverse_events[score]}%')
