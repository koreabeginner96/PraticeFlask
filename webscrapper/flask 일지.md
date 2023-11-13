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

  ### Flask에서 URL 키워드 값 사용하기

- **Flask에 `request` Import 하기**:
  - URL에서 키워드 값을 사용하려면, 먼저 `from flask import request`를 사용하여 `request` 모듈을 임포트해야 합니다.

- **주소에서 파라미터(키워드) 가져오기**:
  - 키워드 값을 가져오려면, `keyword = request.args.get("keyword")`를 사용합니다.
  - 이 코드는 URL 쿼리에서 "keyword"라는 이름의 파라미터 값을 가져옵니다.

- **키워드를 화면에 표출하기**:
  - 메인 함수에서:
    ```python
    keyword = request.args.get("keyword")
    return render_template("search.html", keyword=keyword)
    ```
  - `search.html`에서:
    ```html
    <h1>Search Result for "{{keyword}}":</h1>
    ```
  - 이렇게 하면, `search.html` 페이지에서 "{{keyword}}" 부분에 실제 키워드 값이 표시됩니다.
