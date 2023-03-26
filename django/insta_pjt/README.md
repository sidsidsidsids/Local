# 인스타그램 클론 코딩

- 목표
  
  - django 초기 환경 설정
  
  - CRUD 구현
  
  - 이미지 업로드 (media)
  
  - 로그인/로그아웃/회원가입
    
    - 회원탈퇴/정보수정/PW변경
  
  - bootstrap 활용 웹 디자인

---

### 0325

![0326django_instagram_pjt.JPG](README_assets/43696dcb3cc3e03d2fe7cbd04038e39c904a3084.JPG)

- 구현
  
  - django 초기 구성
  
  - CRUD
  
  - bootstrap navbar, content card

- 제약
  
  - html including 기능 구현하여 index.html 안에 post.html을 넣어 게시글 부분을 따로 받으려 했으나 일단은 index.html 안에서 context로 받아 출력하도록 구현함

- 미완성
  
  - navbar 반응성에서 햄버거 버튼 출력되는데 버튼 자체 기능 구현해야함

---

### 0326

![0326django_instagram_pjt_index_without_login.JPG](README_assets/58f2df79c0f14a1c6ae0f66cb65e275372ffe90c.JPG)

![0326django_instagram_pjt_login.JPG](README_assets/1656f0130ba7716992e3a8b54de1a7d7d9b95f45.JPG)

![0326django_instagram_pjt_index_with_login.JPG](README_assets/e2e5cdb27627b8845f78297b1044bb364024a9d7.JPG)

![0326django_instagram_pjt_edit.JPG](README_assets/b2271e17e4f1f8a5ad585ab04ef5d82d0a5305a3.JPG)

- 구현
  
  - 유저 (로그인, 로그아웃, 회원가입, 정보수정, 비밀번호수정, 회원탈퇴)
    
    - django 이용

- 제약
  
  - forms.py에서 django form 그대로 이용해서 한글로 변환 안함

- 미완성
  
  - 햄버거 버튼
  
  - authenticated한 유저에 대한 content 업로드/삭제 권한
