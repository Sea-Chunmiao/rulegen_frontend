import streamlit as st

def set_model_params(temp: str, top_p: str, top_k: str):
    st.session_state["temp"] = temp
    st.session_state["top_p"] = top_p
    st.session_state["top_k"] = top_k
    
def sidebar():
    with st.sidebar:
        st.markdown("# Configuration")
        
        st.selectbox('Model Choice', ['CodeT5', 'CodeBERT', 'StarCoder'], key="model")
        Temperature_input = st.text_input("Temperature", key="context1")
        Top_p_input = st.text_input("Top P", key="context2")
        Top_k_input = st.text_input("Top K", key="context3")

        if Temperature_input and Top_p_input and Top_k_input:
            set_model_params(Temperature_input, Top_p_input, Top_k_input)
            
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
        'before': st.session_state.get("before_input_text", ""),
        'after': st.session_state.get("after_input_text", ""),
        'context': st.session_state.get("context_input_text", ""),
        }

        data_inf = pd.DataFrame([data_inf])

        if submitted:
            st.session_state["predicted"] = "nihao"
        # Predict using model (Nghi)
        #    y_pred_inf = model.predict(data_inf)
        #    st.write('## Iris Variety = '+ str(y_pred_inf))
        #    st.markdown('---')    