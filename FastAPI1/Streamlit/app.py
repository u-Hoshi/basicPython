import streamlit as st
import pandas as pd
import numpy as np

# st.button("click me")

if st.button("click me"):
    st.write("clicked!!!")

if st.checkbox("click"):
    st.write("checkbox clicked")

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write(f"選択肢{options}")


age = st.sidebar.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

col1,col2 = st.columns(2)
col1.write("col1")
col2.write("col2")