# Growth_crawler
주제: 우리나라의 년도별 경제와 인구성장률 비교



프로젝트 내용:

국가 지표계에서 제공하는 데이터를 이용해 우리나라의 년도별 경제와 인구성장률의 수치를 그래프로 나타내어 비교하고자 한다.

구체적으로 경제성장률과 인구성장률을 크롤링 한다. 년도별 경제성쟝률을 나타내는 그래프 1, 년도별 인구성장률을 나타내는 그래프 2로 matpoltlib를 이용해 표기한다.



202155190 한성문 역할

크롤링 - 국가 지표계에서 제공하는 경제와 인구성장률 데이터의 Beautiful Soup를 이용해 성장률 정보를 포함하고 있는 전체 테이블을 찾아서 반환한다.

그래프 - 유혁진이 반환한 리스트를 이용해 경제성장률과 년도가 출력되는 그래프 1을 생성한다.



202155162 유혁진 역할

크롤링 - 한성문이 찾은 전체 테이블에서 경제성장률과 인구성장률, 그리고 각 년도를 각각 리스트를 만들어 이를 반환한다.

그래프 - 인구성장률과 년도가 출력되는 그래프2를 생성한다.



크롤링할 사이트 URL : http://www.index.go.kr/unify/main.do?clasCd=10
