import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def run_app_eda():
    st.subheader('버섯 데이터 분석')
    
    df = pd.read_csv('data/mushrooms.csv')
    print(df)
    if st.checkbox('데이터 프레임 보기'):
        st.dataframe(df)


    st.subheader('기본 통계 데이터')   
    encoder = LabelEncoder()
    for col in df.columns:   # 문자 -> 숫자로 변경
        df[col]= encoder.fit_transform(df[col])         
    st.dataframe(df.describe())


    st.subheader('독버섯 데이터')


    st.subheader('식용버섯 데이터')


    st.subheader('')