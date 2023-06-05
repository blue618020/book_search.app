import streamlit as st

def run_app_home():
    st.text('- 이 앱은 서울특별시교육청 남산도서관의 장서 대출목록을 검색할 수 있는 앱 대시보드입니다.')
    st.text('- 데이터셋을 이용해 도서명, 저자, 출판사 검색을 지원합니다.')
    st.text('- 남산도서관 홈페이지 : https://nslib.sen.go.kr/')

    st.subheader('사용한 자료')

    st.text('> 서울특별시교육청남산도서관 장서 대출목록 (2023년 04월)')
    st.text('https://www.data4library.kr/openDataV')

    st.subheader('제공하는 내용')
    st.text('도서명, 저자, 출판사, 발행년도, ISBN, 부가기호, 권, 주제분류번호, 도서권수, 대출건수, 등록일자')
    st.text('= 총 420675개의 도서 데이터를 제공합니다.')

    img_url = 'https://nslib.sen.go.kr/board/boardFile/download/428/1027474/189061.do'
    st.image(img_url)

    
