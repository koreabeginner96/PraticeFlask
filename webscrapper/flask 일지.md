### Flask 웹 개발 노트

- **터미널에서 `main.py` 위치로 이동**: 
  `main.py` 위치 찾기 및 작업 지시사항.

- **`@app.route("/")` 데코레이터 사용**: 
  - Flask에서 사용되는 데코레이터입니다.
  - 이 코드 바로 아래에 함수를 위치시킵니다.
  - Flask는 사용자가 route(괄호 안의 주소)의 페이지를 방문할 때 해당 함수를 호출해야 함을 인식합니다.

- **`templates` 폴더 생성**: 
  - 반드시 "templates"라는 이름의 폴더를 생성해야 합니다.
  - Flask는 오직 'templates'라는 이름으로 된 폴더만 찾을 수 있기 때문입니다.
  - 위치도 반드시 `main.py` 옆에 폴더를 생성해야 합니다.

- **`templates`를 Import 하기**: 
  - `from flask import Flask, render_template`를 사용합니다.
  - 예: `return render_template("hello.html")`.

- **HTML 사용법**: 
  - 주석 처리: Ctrl+K+C.
  - HTML 폼 가져오기: `!` + 탭 키.
  - 변수 생성: `{{ }}` 중괄호 두 번 안에 변수를 적습니다.
  - form action="/search" serch한 홈페이지로가게 하는 법