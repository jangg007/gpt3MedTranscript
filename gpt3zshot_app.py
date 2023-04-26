import streamlit as st
import openai

openai.api_key = "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"


@st.cache_resource
def get_model(med_transcript):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"In the text below, what is the patient name, patient demographic, family history, patient history, allergies,vitals, lab reports, medical-procedutes,diseases/illnesses/problems, medicines?\n\ntext: \"Robert is having fever and head ache. He is 52 years old male. He is taking antibiotics and acetaminophen. His mother had a history of hypertension\"\n\nPATIENT-NAME: Robert  \n PATIENT DEMOGRAPHICS: 52 year male  \n  FAMILY HISTORY: Mother had a history of hypertension\nPATIENT HISTORY: Not given\nALLERGIES: Not given\nVITALS: Not given\nLAB REPORTS: Not given\nMEDICAL PROCEDURES: Not given\nDISEASES/ILLNESSES/PROBLEMS:  fever and headache\nMEDICINES: Antibiotics and Acetaminophen\n\n##\n\ntext:{med_transcript}\n\n",
    temperature=0.7,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return response.choices[0].text



med_trans_input = st.text_area("Enter medical Transcript:")
button = st.button("Analyze")

if med_trans_input and button:
    if len(med_trans_input) > 8000:
        st.write("The length of string > 8000")
    else:
        outputs = get_model(med_trans_input)
        for x in outputs.split('\n'):
            st.write(x)
