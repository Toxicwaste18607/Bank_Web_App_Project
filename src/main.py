import os
import streamlit as st 


APP_PATH = os.path.dirname(os.path.abspath(__file__))


def get_data_path(filename: str) -> str:
    '''Returns the path to an asset file, given its filename.'''
    return os.path.join(APP_PATH, "data", filename)



st.title("Personal Banking App")
name = st.text_input ("what is your name")
st.write(name)