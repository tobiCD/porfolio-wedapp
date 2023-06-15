import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")

df=pd.read_csv("data2.csv",sep=",")
col1 , col2 , col3=st.columns([25,25,25])

with col3 :
    for index , row in df[:2].iterrows():
        st.header(row["title"])
        st.write(row["Description"])
        st.image("images/"+row["image"])
        st.write("[More infomation ](https://www.facebook.com/)")

with col2:
    for index , row in df[2:4].iterrows():
        st.header(row["title"])
        st.write(row["Description"])
        st.image("images/"+row["image"])
        st.write("[More infomation ](https://www.facebook.com/)")
with col1:
    for index , row in df[4:8].iterrows():
        st.header(row["title"])
        st.write(row["Description"])
        st.image("images/"+row["image"])
        st.write("[More infomation ](https://www.facebook.com/)")
