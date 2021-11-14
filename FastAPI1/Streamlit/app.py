import streamlit as st
import pandas as pd

st.title("Sample App")

df=pd.DataFrame({
  "一列目":[1,2,3,4],
  "二列目":[-1,-2,-3,-4]
})
st.dataframe(df)

st.json({
  "data":{
    "name":"hoge"
  }
})