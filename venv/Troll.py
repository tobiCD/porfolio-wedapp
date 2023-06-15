import pandas as pd
import streamlit as st
df=pd.read_csv("data2.csv",sep="")
col1 , col2 , col3=st.columns(3)
with col3 ,col2,col1:
    for index , row in df[:7].iterrows():
        st.header(row["title"])
        st.write(row["Description"])
        st.image("images/"+row["image"])
        st.write("[More infomation ](https://www.facebook.com/)")
