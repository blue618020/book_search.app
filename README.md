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

<h4> 메인페이지 </h4>
- 사용한 데이터 출처, 남산도서관 링크, 데이터 컬럼 수와 컬럼의 정보 등 앱 대시보드의 설명이 기재되어있습니다. 

<br>
<h3>EDM</h3>

<h4> 데이터 분석 페이지 </h4>

  - 원본데이터 제목 : 서울특별시교육청남산도서관 장서 대출목록 (2023년 04월).csv
  - 가공한 데이터 제목: ns_book.csv

<br>
<h4> Google Colab 에서 데이터프레임을 가공 </h4>

  - 결측치( isna( ) )를 확인 후, 결측치가 제일 많은 'Unnamed: 13', '세트 ISBN' 컬럼을 drop 한 후 다시 데이터프레임에 덮어씌움
  - 발행년도의 숫자가 아닌 문자를 포함하는 896개의 행을 찾아서 연도 앞과 뒤에 있는 문자 제외시킴
  - 변환되지 않은 NaN 도는 4자리 숫자가 아닌 경우를 찾아서 임의로 -1 값으로 바꾼 후, atype() 매서드로 발행년도 열의 데이터 타입을 정수형인 int32로 변환
  - 연도가 4000이 넘는 130개의 값을 찾아서 -2333 뺄셈 
  - 그 외 연도가 잘못 지정되었거나 알 수 없는 5999개의 데이터를 drop
  - to_csv로 데이터프레임을 다운받아서 사용

<br>
<h4> 전체 도서 목록 데이터프레임 확인 </h4>
  
  - ns_book.csv 데이터프레임을 확인할 수 있습니다.

<br>
<h4> 가장 대출 건수가 많은 도서 순위 </h4>

  - 전체 도서 중, 대출 건수 상위 1위부터 10위까지의 도서 정보를 제공합니다. 
  - slider 를 조절하면 원하는 등수까지만 확인할 수 있습니다.
  - 데이터프레임과 막대그래프로 정보와 등수 그래프를 확인할 수 있습니다.

<br>
<h4> 연도별 발행된 도서 수 </h4>

  - 발행년도의 첫 시작 연도인 1948년부터 2023년까지만 제공합니다.
  - annotate(주석달기)를 사용해서 그래프 안에 3년 단위로 도서 수를 출력합니다.


<br>
<h4> 출판사별 발행된 도서 수 </h4>

  - 전체 출판사 중, 발행 건수 상위 20개의 출판사 목록을 제공합니다.
  - 그래프에 마우스 커서를 올리면 출판사 이름과 개수를 확인할 수 있습니다.
  - 오른쪽 컬럼을 클릭해서 원하는 출판사만 확인할 수 있습니다.
  


<br>
<h3>Search</h3>

- 도서 검색 창
- 원하는 도서 검색가능
