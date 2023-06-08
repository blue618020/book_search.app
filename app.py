import streamlit as st
from app_home import run_app_home
from app_search import run_app_search  
from app_eda import run_app_eda
from streamlit_option_menu import option_menu # 사이드바 메뉴 시각화

def main():
    st.title('🔍남산도서관 도서 검색대')
    
    with st.sidebar:  # 사이드바. 아래는 시각화 코드
        img_url = ('https://nslib.sen.go.kr/resources/homepage/common/img/li_logo_taye2.gif')
        st.image(img_url) # 사이드바 이미지 추가
        choice = option_menu('MENU', ['Home', 'EDA', 'Search'],
                             icons=['bi bi-house', 'bi bi-file-earmark', 'bi bi-search'],
                             menu_icon='bi bi-book',
                             default_index=0)
        # print(choice)
    
    if choice == 'Home':
        run_app_home()

    elif choice == 'Search':
        run_app_search()

    else:
        run_app_eda()

if __name__ == '__main__':
    main()