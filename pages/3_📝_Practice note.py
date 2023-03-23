import streamlit as st
import pandas as pd
import numpy as np

# 출력     
st.title("제목")
st.header("중제목")
st.subheader("소제목")    
    
st.write('일반글1')
st.write('일반글2')
             
st.write("# Header1", unsafe_allow_html=True)  # 마크다운으로 인식
st.write("## Header2", unsafe_allow_html=True)  # 마크다운으로 인식
st.write("### Header3", unsafe_allow_html=True)  # 마크다운으로 인식
st.markdown("**볼드체**") 
             

def get_data():
    df = pd.DataFrame({
        "A": np.arange(0, 10, 1), 
        "B": np.arange(0, 1, 0.1), 
    })
    return df

data = get_data()
st.write(data)
st.dataframe(data)
st.table(data)