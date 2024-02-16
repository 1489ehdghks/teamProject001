# API 목록

<br/>

### 1. 팀원조회
GET /

   서버 동작 시 메인페이지로 이동
   
<br/>

### 2. 상세 팀원조회


GET /members/<username<username>>/details


   Param ( username : String * 필수)

<br/>

### 3. 팀원 추가 및 수정


POST /members/create/


       Body {
       id (Integer,primary_key=True)
       username String(100,nullable=False)
       image_url String(10000,nullable=False)
       mbti String(100,nullable=False)
       collabo_style String(100,nullable=False)
       advantage String(100,nullable=False)
       blog_url String(10000,nullable=False)
       }


   1) username으로 구별하여 기존에 username이 없으면 팀원 데이터를 추가


   2) username으로 구별하여 기존에 username이 있는 데이터면 기존 데이터를 수정

<br/>

### 4. 팀원 삭제

   POST /members/<username<username>>/delete
   
   Param ( username : String * 필수)
