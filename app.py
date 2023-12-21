import streamlit as st

# Title and introduction
st.title('Canadian Syncope Risk Score Calculator')
st.write('This tool calculates the risk of serious adverse events after syncope.')

# Creating a form for user input
with st.form('risk_score_form'):
    st.subheader('Clinical Evaluation')
    predisposition_to_vasovagal_symptoms = st.selectbox(
        'Predisposition to Vasovagal Symptoms:',
        options=['No', 'Yes'],
        format_func=lambda x: 'No' if x == 'No' else 'Yes, -1 Point'
    )
    history_of_heart_disease = st.checkbox('History of Heart Disease (+1 Point)')
    systolic_bp_reading = st.number_input(
        'Any Systolic Pressure Reading <90 or >180 mmHg (+2 Points)',
        min_value=0, max_value=300, step=1
    )

    st.subheader('Investigations')
    elevated_troponin_level = st.checkbox('Elevated Troponin Level (+2 Points)')
    abnormal_qrs_axis = st.checkbox('Abnormal QRS Axis (+1 Point)')
    qrs_duration = st.checkbox('QRS Duration >130 ms (+1 Point)')
    corrected_qt_interval = st.checkbox('Corrected QT Interval >480 ms (+2 Points)')

    st.subheader('Diagnosis in Emergency Department')
    diagnosis = st.radio(
        'Diagnosis:',
        options=['Vasovagal Syncope', 'Cardiac Syncope', 'Neither'],
        index=2,
        format_func=lambda x: f'{x} ({"-2 Points" if x == "Vasovagal Syncope" else "+2 Points" if x == "Cardiac Syncope" else "0 Point"})'
    )

    submit_button = st.form_submit_button('Calculate Risk Score')

if submit_button:
    score = 0
    # Clinical evaluation
    if predisposition_to_vasovagal_symptoms == 'Yes':
        score -= 1
    if history_of_heart_disease:
        score += 1
    if systolic_bp_reading < 90 or systolic_bp_reading > 180:
        score += 2

    # Investigations
    if elevated_troponin_level:
        score += 2
    if abnormal_qrs_axis:
        score += 1
    if qrs_duration:
        score += 1
    if corrected_qt_interval:
        score += 2

    # Diagnosis in the emergency department
    if diagnosis == 'Vasovagal Syncope':
        score -= 2
    elif diagnosis == 'Cardiac Syncope':
        score += 2

    # Calculate risk category
    risk_category = ''
    if score <= -3:
        risk_category = 'Very Low'
    elif score <= 0:
        risk_category = 'Low'
    elif score <= 3:
        risk_category = 'Medium'
    elif score <= 6:
        risk_category = 'High'
    else:
        risk_category = 'Very High'

    # Display the results
    st.write(f'Your Canadian Syncope Risk Score is: {score}')
    st.write(f'Estimated Risk Category: {risk_category}')

