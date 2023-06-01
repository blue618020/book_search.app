import streamlit as st
import pandas as pd

def run_app_eda():
    st.subheader('전체 도서 목록 확인')
    df = pd.read_csv('data/서울특별시교육청남산도서관 장서 대출목록 (2023년 04월).csv',
                     encoding='EUC-KR', low_memory=False, index_col=0)
    df = df.drop(['Unnamed: 13', '세트 ISBN'], axis=1) 
    print(df)
    if st.checkbox('◀ 클릭'):
        st.dataframe(df)
        
    st.subheader('가장 대출 건수가 많은 도서 Top3')
    df2 = df.sort_values('대출건수', ascending=False)
    df2 = df2[['대출건수', '도서명', '저자', '출판사', '발행년도', 'ISBN', '부가기호', 
     '권', '주제분류번호', '도서권수', '등록일자']].head(3)
    st.dataframe(df2)

    