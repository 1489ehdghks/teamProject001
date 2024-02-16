API 목록


1. 목록조회
GET /members/<username>/
<br/>
<br/>
3. 상세 목록조회
   GET /members/<username>/details
     Param ( username : String * 필수)
<br/>
<br/>
4. 팀원 추가 및 수정
   POST,GET /members/create/
<br/>
   
       Body {
       id (Integer,primary_key=True)
       username String(100,nullable=False)
       image_url String(10000,nullable=False)
       mbti String(100,nullable=False)
       collabo_style String(100,nullable=False)
       advantage String(100,nullable=False)
       blog_url String(10000,nullable=False)
       }

<br/>
<br/>
   1) GET
     username으로 구별하여 기존에 username이 없으면 GET을 진행
<br/>
<br/>
   2) POST
      username으로 구별하여 기존에 username이 있는 데이터면 POST를 진행.

<br/>
<br/>
6. 팀원 삭제
   DELETE /members/<username>/delete
     Param ( username : String * 필수)
