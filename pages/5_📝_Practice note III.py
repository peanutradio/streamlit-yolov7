import streamlit as st
import pandas as pd
import numpy as np

# Slider
st.header('slide')
v = st.slider("X", 1, 10) # 숫자 1 ~ 10을 선택할 수 있는 slider (이벤트)
st.write('선택된 값: '+str(v)) # 이벤트가 발생하면 코드를 처음부터 다시 실행시킨다.

# 입력창
st.header('input text')
v2 = st.text_input('이름')
st.write('이름: '+v2)

# 체크박스
## 함수를 계속 실행 시켜주는 것이 아니라 return 데이터를 메모리에 따로 저장해 놓은 후 불러올 때만 가지고 온다 -> 코드가 실행되는 시간을 줄여준다.
### 데이터는 cache_data, 모델은 cache_resource
@st.cache_data
def get_data():
    df = pd.DataFrame({
        "A":np.arange(0, 10, 1),
        "B":np.arange(0, 1, 0.1)
    })
    return df

bool_value = st.checkbox('Show DataFrame') # Check가 되면 True, 아니면 False
df = get_data()
if bool_value:
    st.dataframe(df)
else:
    st.write('데이터가 없습니다')