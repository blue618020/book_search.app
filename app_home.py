import streamlit as st

def run_app_home():
    st.text('- 이 앱은 서울특별시교육청 남산도서관의 장서 대출목록을 검색할 수 있는 앱 대시보드입니다.')
    st.text('- 데이터셋을 이용해 도서명, 저자, 출판사 검색을 지원합니다.')

    img_url = 'https://nslib.sen.go.kr/board/boardFile/download/428/1027474/189061.do'
    st.image(img_url)

    
