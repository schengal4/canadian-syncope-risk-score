import streamlit as st

st.title('Canadian Syncope Risk Score Calculator')
st.write('This calculator helps to identify patients with syncope at risk of serious adverse events within 30 days after disposition from the emergency department.')


with st.form('risk_score_form'):
    st.subheader('Clinical Evaluation')
    predisposition_to_vasovagal_symptoms = st.radio('Predisposition to vasovagal symptoms', ['Yes', 'No'])
    history_of_heart_disease = st.radio('History of heart disease', ['Yes', 'No'])
    systolic_bp_reading = st.radio('Any systolic blood pressure reading < 90 or > 180 mm Hg', ["Yes", "No"])

    st.subheader('Investigations')
    elevated_troponin_level = st.radio('Elevated troponin level', ['Yes', 'No'])
    abnormal_qrs_axis = st.radio('Abnormal QRS axis', ['Yes', 'No'])
    qrs_duration = st.radio('QRS duration > 130 ms', ['Yes', 'No'])
    corrected_qt_interval = st.radio('Corrected QT interval > 480 ms', ['Yes', 'No'])

    st.subheader('Diagnosis in Emergency Department')
    vasovagal_syncope = st.radio('Vasovagal syncope', ['Yes', 'No'])
    cardiac_syncope = st.radio('Cardiac syncope', ['Yes', 'No'])

    submitted = st.form_submit_button('Calculate Risk Score')

def calculate_risk_score(inputs):
    score = 0
    score += -1 if inputs['predisposition_to_vasovagal_symptoms'] == 'Yes' else 0
    score += 1 if inputs['history_of_heart_disease'] == 'Yes' else 0
    score += 2 if inputs['systolic_bp_reading'] == "Yes" else 0
    score += 2 if inputs['elevated_troponin_level'] == 'Yes' else 0
    score += 1 if inputs['abnormal_qrs_axis'] == 'Yes' else 0
    score += 1 if inputs['qrs_duration'] == 'Yes' else 0
    score += 2 if inputs['corrected_qt_interval'] == 'Yes' else 0
    score += -2 if inputs['vasovagal_syncope'] == 'Yes' else 0
    score += 2 if inputs['cardiac_syncope'] == 'Yes' else 0
    return score
def determine_risk_category(risk_score):
    if risk_score <= -2:
        risk_category = "Very Low"
    elif -1 <= risk_score <= 0:
        risk_category = "Low"
    elif 1 <= risk_score <= 3:
        risk_category = "Medium"
    elif 4 <= risk_score <= 5:
        risk_category = "High"
    else:
        risk_category = "Very High"
    return risk_category
def calculate_risk_percentage(risk_score):
    risk_score_to_percentage = {-3: 0.4, -2: 0.7, -1: 1.2, 0: 1.9, 1: 3.1, 2: 5.1, 3: 8.1, 4: 12.9, 5: 19.7, 
                                6: 28.9, 7: 40.3, 8: 52.8, 9: 65.0, 10: 75.5, 11: 83.6}
    return risk_score_to_percentage[risk_score]

if submitted:
    risk_inputs = {
        'predisposition_to_vasovagal_symptoms': predisposition_to_vasovagal_symptoms,
        'history_of_heart_disease': history_of_heart_disease,
        'systolic_bp_reading': systolic_bp_reading,
        'elevated_troponin_level': elevated_troponin_level,
        'abnormal_qrs_axis': abnormal_qrs_axis,
        'qrs_duration': qrs_duration,
        'corrected_qt_interval': corrected_qt_interval,
        'vasovagal_syncope': vasovagal_syncope,
        'cardiac_syncope': cardiac_syncope
    }

    risk_score = calculate_risk_score(risk_inputs)
    risk_category = determine_risk_category(risk_score)
    risk_percentage = calculate_risk_percentage(risk_score)
    
    st.write(f'Calculated Risk Score: {risk_score}')
    st.write(f'Risk Category: {risk_category}')
    st.write(f'Estimated risk of serious adverse events: {risk_percentage}')


