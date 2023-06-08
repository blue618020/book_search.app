import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# 한글폰트 설정 코드
# Streamlit File *.py
import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

def run_app_eda():
    st.subheader('전체 도서 목록 확인📚')
    df = pd.read_csv('data/ns_book.csv', low_memory=False)
    st.dataframe(df[:10])  
    st.text('= 전체 426795 rows × 11 columns')  

    st.subheader(' ') # 간격띄움

    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())


    st.subheader(' ')
    st.subheader(' ') # 간격띄움

    st.subheader('가장 대출 건수가 많은 도서 순위')
    st.text('상위 1위부터 10위까지 확인할 수 있습니다.')
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
    # plt.rcParams['font.family']='Malgun Gothic' # 깨짐 방지 폰트 설정(맑은고딕은 되는데)
    plt.rcParams['font.family']='NanumGothic'  # 나눔고딕은 여기선 안됨(리눅스 서버에선 됨)

    plt.xticks(rotation = 45)   # 글씨 겹침 방지. x축으로 45도 돌림
    plt.title('대출 건수 순위', fontsize=20)
    plt.bar(df3['도서명'], df3['대출건수'])
    st.pyplot(fig)


    st.subheader(' ')
    st.subheader(' ') # 간격띄움

    st.subheader('연도별 발행된 도서 수')
    st.text('> 데이터의 첫 시작 연도인 1948년부터 2023년까지 확인할 수 있습니다.')
    st.text('그래프 안 숫자는 3년 단위로 나오는 도서 수 입니다.')
    count_by_year = df['발행년도'].value_counts().sort_index()
    count_by_year = count_by_year[count_by_year.index <= 2023]

    # 연도별 발행된 도서 수 선 그래프
    fig2 = plt.figure(figsize=(10,5))   
    plt.plot(count_by_year, marker='.')
    for idx, val in count_by_year[::3].items():
        plt.annotate(val,(idx,val))
    plt.title('연도별 발행된 도서 수', fontsize=20)
    plt.xlabel('year')
    plt.ylabel('books')
    st.pyplot(fig2)

    # print(count_by_year.max())
    st.text('= 가장 많이 발행된 도서 수는 2014년에 '+ str(count_by_year.max()) + '권 입니다.')


    st.subheader(' ')
    st.subheader(' ') # 간격띄움

    st.subheader('출판사별 발행된 도서 수')
    st.text('> 전체 출판사 중 발행된 도서 수가 많은 상위 20개의 출판사 목록만 제공합니다.')
    st.text('그래프에 마우스 커서를 올리면 출판사 이름과 개수를 확인할 수 있습니다.')
    top20 = df['출판사'].value_counts()[:20] # 상위 20개 출판사 목록
    top20_df = top20.to_frame()  # 데이터팜으로 만듬
    top20_df.reset_index(inplace=True)  # 인덱스초기화
    top20_df.columns = ['출판사', '개수']  # 컬럼 이름 변경

    fig4 = px.pie(top20_df, '출판사', '개수', title='출판사 도서 비율')
    st.plotly_chart(fig4)
    st.text('= 가장 많이 도서를 발행한 출판사는 '+ str(top20.max()) +'권의 문학동네 입니다.')



    # 폰트 저장경로 확인한 코드
    # import matplotlib
    # print(matplotlib.__version__) # matplotlib 버전확인
    # print(matplotlib.__file__) # 설치 폴더 경로 확인
    # print(matplotlib.get_cachedir()) # 캐시 폴더 경로 확인