import streamlit as st
import pickle

model = pickle.load(open('smish_detector.pkl', 'rb'))

def predict_smishing(text):
    result = model.predict([text])
    return result[0]

st.title('Smishing Detector Demo')
st.write('This is a demo for a smishing detector model.')

text = st.text_area('Enter your text here:')

if st.button('Detect'):
    result = predict_smishing(text)
    if result == 1:
        st.write('This is a potetnial smishing message.')
    else:
        st.write('This is not a smishing message.')