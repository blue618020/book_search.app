import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run_app_eda():
    st.subheader('전체 도서 목록 확인📚')
    df = pd.read_csv('data/서울특별시교육청남산도서관 장서 대출목록 (2023년 04월).csv',
                     encoding='EUC-KR', low_memory=False, index_col=0)
    df = df.drop(['Unnamed: 13', '세트 ISBN'], axis=1) 
    print(df)
    if st.checkbox('◀ 클릭'):
        st.dataframe(df)
        

    st.subheader('가장 대출 건수가 많은 도서 순위🏅')
    number = st.slider('순위 드래그 ▼', min_value=3, max_value=10, step=1, value=5)
    print(number)  # 원하는 순위 입력받기

    df2 = df.sort_values('대출건수', ascending=False)
    df3 = df2[['대출건수', '도서명', '저자', '출판사', '발행년도', 'ISBN', '부가기호', 
     '권', '주제분류번호', '도서권수', '등록일자']].head(number)
    st.dataframe(df3)


    # 대출건수 순위 그래프
    df4 = df2.head(number)
    df4.loc[122928,'도서명'] = '사피엔스:' # 대출건수 1위의 이름이 너무 길어서 임의로 줄임..

    fig = plt.figure(figsize=(10,5))
    plt.rcParams['font.family']='Malgun Gothic'  # 깨짐 방지 폰트 설정
    plt.xticks(rotation = 45)   # 글씨 겹침 방지. x축으로 45도 돌림
    plt.title('대출 건수 순위', fontsize=20)
    plt.bar(df4['도서명'], df4['대출건수'])
    st.pyplot(fig)


