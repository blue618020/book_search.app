import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run_app_eda():
    st.subheader('전체 도서 목록 확인📚')
    df = pd.read_csv('data/ns_book.csv')
    if st.checkbox('◀ 클릭'):
        st.dataframe(df)
        

    st.subheader('가장 대출 건수가 많은 도서 순위🏅')
    number = st.slider('순위 드래그 ▼', min_value=3, max_value=10, step=1, value=5)
    # print(number)  # 원하는 순위 입력받기

    df = df.sort_values('대출건수', ascending=False)
    df2 = df[['대출건수', '도서명', '저자', '출판사', '발행년도', 'ISBN', '부가기호', 
     '권', '주제분류번호', '도서권수', '등록일자']].head(number)
    st.dataframe(df2)



    # 대출건수 순위 막대 그래프
    df3 = df2.head(number)
    df3.loc[121616,'도서명'] = '사피엔스:' # 대출건수 1위의 이름이 너무 길어서 임의로 줄임..
    fig = plt.figure(figsize=(10,5))
    # 폰트가 말썽이야!!!!!1
    plt.rcParams['font.family']='Malgun Gothic' # 깨짐 방지 폰트 설정(맑은고딕은 되는데)
    #plt.rcParams['font.family']='NanumGothic'  # 나눔고딕 설정 중...

    plt.xticks(rotation = 45)   # 글씨 겹침 방지. x축으로 45도 돌림
    plt.title('대출 건수 순위', fontsize=20)
    plt.bar(df3['도서명'], df3['대출건수'])
    st.pyplot(fig)



    st.subheader('연도별 발행된 도서')
    st.text('> 1948 ~ 2023년까지')
    count_by_year = df['발행년도'].value_counts()
    count_by_year = count_by_year.sort_index()
    count_by_year = count_by_year[count_by_year.index <= 2023]

    # 연도별 발행된 도서 수 선 그래프
    fig2 = plt.figure(figsize=(10,5))    
    plt.plot(count_by_year, marker='.')
    for idx, val in count_by_year[::5].items():
        plt.annotate(val,(idx,val))
    plt.title('연도별 발행된 도서 수', fontsize=20)
    plt.xlabel('연도')
    plt.ylabel('도서')
    st.pyplot(fig2)



    st.subheader('출판사별 발행된 도서')
    st.text('> 1948 ~ 2023년까지')
    top20 = df['출판사'][:20] 
    column_list = st.multiselect('컬럼을 선택하세요',top20)
    print(column_list)

    # line1 = df[df[column_list]]
    fig3, ax = plt.subplots(figsize=(10,8))
    #ax.plot(['발행년도'], ['대출건수'])
    st.pyplot(fig3)


    # import matplotlib
    # print(matplotlib.__version__) # matplotlib 버전확인
    # print(matplotlib.__file__) # 설치 폴더 경로 확인
    # print(matplotlib.get_cachedir()) # 캐시 폴더 경로 확인