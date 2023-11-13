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
### Flask에서 키워드를 이용한 추출기 활용하기

- **추출기 모듈 Import 하기**:
  - Indeed와 WWR 추출기를 사용하기 위해 다음과 같이 import 합니다:
    ```python
    from extractors.indeed import extract_indeed_jobs
    from extractors.wwr import extract_wwr_jobs
    ```

- **키워드를 이용한 추출기 함수 사용**:
  - URL에서 키워드 값을 가져와 추출기에 사용합니다:
    ```python
    keyword = request.args.get("keyword")
    indeed_jobs = extract_indeed_jobs(keyword)
    wwr_jobs = extract_wwr_jobs(keyword)
    jobs = indeed_jobs + wwr_jobs
    ```

- **결과를 HTML 페이지에 전달**:
  - `return` 구문에서 `jobs`를 `render_template`에 전달합니다:
    ```python
    return render_template("your_template.html", jobs=jobs)
    ```

- **HTML에서 데이터 사용하기**:
  - `for` 루프를 사용하여 `jobs` 내의 각 작업을 표시합니다:
    ```html
    {% for job in jobs %}
      <!-- 여기에 각 job을 표시하는 HTML 코드 -->
    {% endfor %}
    ```
  - `{{ }}`: Flask가 변수 값을 HTML에 실제로 렌더링합니다.
  - `{% %}`: Python 코드를 HTML 내에 포함시킬 때 사용합니다.

### Pico CSS 사용하기

- **Pico CSS 설치**:
  - Pico CSS는 작은 양의 CSS로 웹 페이지를 보기 좋게 만들어줍니다.
  - 설치를 위해 CDN 링크를 복사한 후 HTML의 `<head>` 부분에 붙여넣습니다.

- **Layout 기초**:
  - Pico CSS에는 몇 가지 간단한 레이아웃 기술이 있습니다.
  - **Container**: 요소를 중앙에 배치하려면, `<main class="container">` 안에 내용을 넣습니다.
    ```html
    <body>
      <main class="container">
        <!-- 내용 -->
      </main>
    </body>
    ```

- **Table 사용**:
  - 테이블을 사용하여 데이터를 정렬된 형식으로 표시할 수 있습니다.
    ```html
    <table>
        <thead>
            <tr>
                <th>Position</th>
                <th>Company</th>
                <th>Location</th>
                <th>Link</th>
            </tr>
        </thead>
        <tbody>
            {% for job in jobs %}
            <tr>
                <td>{{ job.position }}</td>
                <td>{{ job.company }}</td>
                <!-- 나머지 데이터 표시 -->
            </tr>
            {% endfor %}
        </tbody>
    </table>
    ```

- **테이블의 추가 스타일링**:
  - **가로 줄**: `<table role="grid">`를 사용하여 테이블에 가로 줄을 추가할 수 있습니다.
  - **가로 스크롤**: `<figure>` 태그 안에 테이블을 넣어 가로 스크롤을 추가할 수 있습니다.

