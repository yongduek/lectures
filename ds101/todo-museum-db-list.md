
# 박물관 소장품 이미지 정보

- 여기서 가지고 올수 있다: [공공데이터 포털, 박물관 소장품 이미지 정보](https://www.data.go.kr/dataset/3070607/fileData.do)
- 유물명, 이명칭, 한자명칭, 국적시대, 재질, 이미지 파일명, 페이지경로
- 모두 7626개에 대한 정보. 이미지파일은 1660개만 images 폴더에 jpg 파일로 제공.
- 페이지경로가 잘못 된 것들이 있다.
- 이미지 파일이 없는 것들이 있다.
- 이미지는 있으나 db list에는 없는 경우도 있다


## Projects Possible:

1. Explorative Research

        1. do it yourself and report
        1. histogram for 재질, 국적, 명청/이명칭/한자명칭
        2. counting 갯수 세기
        
1. Labeled/Supervised

        1. images 폴더에 이미지가 존재하는 유물 정보만 필터링하여 리스트 만들기
        2. 불상만 골라내기. 도자기 (그릇이나 병) 종류만 골라내기
        3. 통일신라와 조선시대 물품으로 구분하기
        4. 

1. Unlabeled/Unsupervised

        1. t-SNE 로 전체 물품의 2차원 분포표 제작하기
                - 사용가능 입력단위: 이미지, 유물명
                
1. Design: What service can we do?

        1. image categorizer (input: image, output: category & similar images)
        

1. Project++

        1. images 폴더에 없는 이미지를 유물명으로 검색하여 자료보충하기
                - 국립중앙박물관 홈페지 이용
                - 구글 검색
                - 데이터베이스의 이미지파일명, 페이지경로 업데이트하기
                
        1. 고화질 데이터로 자료 보충하기
                - How?
                
        1. Making the Project Useful 
                - contact `www.data.or.kr` or 국립중앙박물관
        
        1. 불상 데이터베이스 + 불상얼굴 패턴 비교
                - storytelling
        
        1. 수막새 데이터베이스 만들기와 패턴 비교
        
        
