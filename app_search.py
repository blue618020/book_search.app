import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def run_app_search():
        
    df = pd.read_csv('data/서울특별시교육청남산도서관 장서 대출목록 (2023년 04월).csv',
                     encoding='EUC-KR', low_memory=False, index_col=0)
    df = df.drop(['Unnamed: 13', '세트 ISBN'], axis=1) 
    print(df)
    if st.checkbox('전체 도서 목록 확인'):
        st.dataframe(df)


    st.subheader('도서 검색')
    book_name = st.text_input('찾고싶은 도서명을 입력하세요.')
    if len(book_name) != 0:
        sum = df['도서명'].str.contains(book_name).sum()
        st.text(str(sum)+'개의 검색 결과 : ')
        st.dataframe(df.loc[df['도서명'].str.contains(book_name, na=False)])


    st.subheader('저자 검색')
    writer_name = st.text_input('찾고싶은 저자명을 입력하세요.')
    if len(writer_name) != 0:
        sum = df['저자'].str.contains(writer_name).sum()
        st.text(str(sum)+'개의 검색 결과 : ')
        st.dataframe(df.loc[df['저자'].str.contains(writer_name, na=False)])

    
    st.subheader('출판사 검색')
    n_name = st.text_input('찾고싶은 출판사를 입력하세요.')
    if len(n_name) != 0:
        sum = df['출판사'].str.contains(n_name).sum()
        st.text(str(sum)+'개의 검색 결과 : ')
        st.dataframe(df.loc[df['출판사'].str.contains(n_name, na=False)])

