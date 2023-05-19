import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import os

from sidebar import sidebar
from utils import (
    parse_txt,
)

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Txl Rule Generation", layout="wide")

# hide_default_format = """
#        <style>
#        #MainMenu {visibility: hidden; }
#        footer {visibility: hidden;}
#        </style>
#        """
# st.markdown(hide_default_format, unsafe_allow_html=True)

st.title('Txl Rule Generation')
st.markdown('This is a workbench for predicting missing TXL rules. You can upload **code before, code after and context rules files** to predict the missing one rule.')

# sidebar()

st.markdown("## Code before")
def clear_submit():
    st.session_state["submit"] = False
 
uploaded_before_file = st.file_uploader(
    label="You can upload a .txt file here",
    type=["txt"],
    accept_multiple_files=False,
    # help="Scanned documents are not supported yet!",
    on_change=clear_submit,
)

before_doc = None
if uploaded_before_file is not None:
    # if uploaded_before_file.name.endswith(".pdf"):
    #     doc = parse_pdf(uploaded_before_file)
    # elif uploaded_before_file.name.endswith(".docx"):
    #     doc = parse_docx(uploaded_before_file)
    if uploaded_before_file.name.endswith(".txt"):
        before_doc = parse_txt(uploaded_before_file)
    else:
        raise ValueError("File type not supported!")
    # before_text = text_to_docs(before_doc)

before_input_text = st.text_area("OR you can input the code here", key="before", on_change=clear_submit)
# ---------------------------
st.markdown("## Code after")
    
uploaded_after_file = st.file_uploader(
    "Please upload a **code after** file with .txt extension",
    type=["txt"],
    accept_multiple_files=False,
    # help="Scanned documents are not supported yet!",
    on_change=clear_submit,
)

after_doc = None
if uploaded_after_file is not None:
    if uploaded_after_file.name.endswith(".txt"):
        after_doc = parse_txt(uploaded_after_file)
    else:
        raise ValueError("File type not supported!")
    # after_text = text_to_docs(after_doc)

after_input_text = st.text_area("OR you can input the code here", key="after", on_change=clear_submit)
# ---------------------------
st.markdown("## Context rules")
    
uploaded_context_file = st.file_uploader(
    "Please upload a **context rules** file with .txt extension",
    type=["txt"],
    accept_multiple_files=False,
    # help="Scanned documents are not supported yet!",
    on_change=clear_submit,
)

context_doc = None
if uploaded_context_file is not None:
    if uploaded_context_file.name.endswith(".txt"):
        context_doc = parse_txt(uploaded_context_file)
    else:
        raise ValueError("File type not supported!")
    # context_text = text_to_docs(context_doc)

context_input_text = st.text_area("OR you can input the code here", key="context", on_change=clear_submit)


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# with st.container():
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.text('TXL rule generation')
#     with right_column:
#         st.text('TXL rule generation')

# code1 = '''pip3 install streamlit'''
# st.code(code1, language='bash')
# ---------------------------

#with st.form(key = "form1"):
my_form = st.form(key = "form1")
# name = my_form.text_input(label = "Please choose the model to predict")
st.selectbox('Please choose the model to predict the missing rule', ['CodeT5', 'CodeBERT', 'StarCoder'], key="model")
# number = my_form.slider("Enter your age", min_value=10, max_value = 100 )
# submit = my_form.form_submit_button(label = "Submit this form")
    
# ----------------------------------------------
# Load Model (Nghi)
import pandas as pd
# import pickle

# model = pickle.load(open('logreg_model.pkl', 'rb'))

# Form
# with st.form(key='form_parameters'):
#    sepal_length = st.slider('Sepal Length', 4.0, 8.0, 4.0)
#    sepal_width = st.slider('Sepal Width', 2.0, 4.5, 2.0)
#    petal_length = st.slider('Petal Length', 1.0, 7.0, 1.0)
#    petal_width = st.slider('Petal Width', 0.1, 2.5, 0.1)
#    st.markdown('---')
   
submitted = st.button('Predict')
   
# Data Inference
data_inf = {
   'before': before_input_text,
   'after': after_input_text,
   'context': context_input_text
}

data_inf = pd.DataFrame([data_inf])

if submitted:
    st.write('## The predicted missing rule is as below: ')
   # Predict using model (Nghi)
#    y_pred_inf = model.predict(data_inf)
#    st.write('## Iris Variety = '+ str(y_pred_inf))
    
   
#  BY courtesy of these articles:  
#  https://medium.com/@imanuelyosi/deploy-your-streamlit-web-app-using-hugging-face-7b9cddb11148
#  https://github.com/Sven-Bo/personal-website-streamlit/tree/master
#  https://github.com/leo-usa/knowledge_gpt/blob/main/knowledge_gpt/main.py