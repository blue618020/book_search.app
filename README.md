![header](https://capsule-render.vercel.app/api?text=Book%20Search&&fontAlignY=40&desc=원하는%20도서를%20검색해보자!&descSize=23&descAlignY=56&fontColor=ffffff&type=waving&color=B897FF&height=280&section=header&%20render&fontSize=80)

<div align=center>
  <h2>사용한 프로그램💻</h2>  
  <img src="https://img.shields.io/badge/GoogleColab-F9AB00?style=flat&logo=googlecolab&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=white"/>
  <img src="https://img.shields.io/badge/AmazonAWS-232F3E?style=flat&logo=amazonaws&logoColor=white"/>
</div>

<br>
<h2>프로젝트 소개</h2>

- 서울특별시교육청 남산도서관의 장서 대출목록을 검색할 수 있는 앱 대시보드입니다.
- 사용한 데이터 출처 : 
<a href="https://www.data4library.kr/openDataL"> 도서관 정보나루 </a>

<br>
<h2>주요 기능</h2> 

- 웹 페이지 이동 링크
- 원하는 도서의 제목을 입력하면 연관된 도서목록이 나오는 기능 제공
- 대출 건수가 많은 도서 순위 제공
- 연도&출판사별 발행된 도서 수 제공

<br>
<h2>페이지 구성</h2>  
<h3>Home</h3>

- 메인페이지
- 사용한 데이터 출처, 남산도서관 링크, 데이터 컬럼 수와 컬럼의 정보 등 앱 대시보드의 설명이 기재되어있습니다. 

<br>
<h3>EDM</h3>

- 데이터 분석 페이지
- 원본데이터 제목 : 서울특별시교육청남산도서관 장서 대출목록 (2023년 04월).csv
- 가공한 데이터 제목: ns_book.csv
- Google Colab 에서 데이터를 가공. 
  - 결측치(isna())를 확인 후, 결측치가 제일 많은 'Unnamed: 13', '세트 ISBN' 컬럼을 drop 한 후 다시 데이터프레임에 덮어씌움
  - 발행년도의 숫자가 아닌 문자를 포함하는 모든 행을 찾아서 

- 전체 도서 목록 데이터프레임 
- 

<br>
<h3>Search</h3>

- 도서 검색 창
- 원하는 도서 검색가능
