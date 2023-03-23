
import streamlit as st
import pandas as pd
import numpy as np

col1, col2 = st.columns(2)
# 출력
             
col1.title("제목")
col1.header("중제목")
col1.subheader("소제목")    
    
col1.write('일반글1')
col1.write('일반글2')
             
col1.write("# Header1")  # 마크다운으로 인식
col1.write("## Header2")  # 마크다운으로 인식
col1.write("### Header3")  # 마크다운으로 인식
col1.markdown("**볼드체**") 
             


col1, col2 = st.columns(2)

def get_data():
    df = pd.DataFrame({
        "A": np.arange(0, 10, 1), 
        "B": np.arange(0, 1, 0.1), 
    })
    return df

def get_data2():
    df2 = pd.DataFrame({
        "A": np.arange(10,20,1),
        "B": np.arange(1.0, 2, 0.1)
    })
    return df2

data = get_data()
data2 = get_data2()
col1.dataframe(data)
col2.dataframe(data2)
st.table(data)