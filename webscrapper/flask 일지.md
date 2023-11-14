# Flask 웹 개발 노트

## Flask 기본 명령어

- **터미널에서 `main.py` 위치로 이동**: 
  `main.py`의 위치를 찾고 작업 지시사항을 따릅니다.

- **`@app.route("/")` 데코레이터 사용**: 
  - Flask에서 사용되는 데코레이터입니다.
  - 이 코드 바로 아래에 함수를 배치합니다.
  - 사용자가 괄호 안의 주소에 해당하는 페이지를 방문할 때 해당 함수를 호출하도록 Flask가 인식합니다.

## 템플릿 관리

- **`templates` 폴더 생성**: 
  - "templates"라는 이름의 폴더를 반드시 생성해야 합니다.
  - Flask는 'templates'라는 이름의 폴더만 인식할 수 있습니다.
  - 폴더는 `main.py` 옆에 생성해야 합니다.

- **`templates` 가져오기**: 
  - `from flask import Flask, render_template`를 사용합니다.
  - 예시: `return render_template("hello.html")`.

## HTML 사용법

- **주석 처리**: Ctrl+K+C.
- **HTML 폼 가져오기**: `!` + 탭 키.
- **변수 생성**: `{{ }}` 중괄호 안에 변수를 넣습니다.
- **Form Action 사용**: `action="/search"`를 사용하여 검색한 페이지로 이동합니다.

## Flask에서 URL 키워드 값 사용

- **Flask에 `request` 가져오기**:
  - URL에서 키워드 값을 사용하려면, `from flask import request`를 사용하여 `request` 모듈을 가져와야 합니다.

- **주소에서 파라미터(키워드) 가져오기**:
  - `keyword = request.args.get("keyword")`를 사용하여 키워드 값을 가져옵니다.
  - 이 코드는 URL 쿼리에서 "keyword"라는 이름의 파라미터 값을 가져옵니다.

- **화면에 키워드 표출하기**:
  - 메인 함수에서:
    ```python
    keyword = request.args.get("keyword")
    return render_template("search.html", keyword=keyword)
    ```
  - `search.html`에서:
    ```html
    <h1>Search Result for "{{keyword}}":</h1>
    ```
  - 이렇게 하면 `search.html` 페이지에서 "{{keyword}}" 부분에 실제 키워드 값이 표시됩니다.

## Flask에서 키워드를 이용한 추출기 활용

- **추출기 모듈 가져오기**:
  - Indeed와 WWR 추출기를 사용하기 위해 다음과 같이 가져옵니다:
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

- **HTML 페이지에 결과 전달**:
  - `return` 구문에서 `jobs`를 `render_template`에 전달합니다:
    ```python
    return render_template("your_template.html", jobs=jobs)
    ```
# HTML에서 데이터 사용하기

- **데이터 표시를 위한 HTML 코드**:
  - `jobs` 내의 각 작업을 `for` 루프를 사용하여 표시합니다:
    ```html
    {% for job in jobs %}
      <!-- 여기에 각 job을 표시하는 HTML 코드 -->
    {% endfor %}
    ```
  - `{{ }}`: Flask에서 변수 값을 HTML에 실제로 렌더링할 때 사용합니다.
  - `{% %}`: Python 코드를 HTML 내에 포함시키기 위해 사용합니다.

### Pico CSS 사용하기

- **Pico CSS 설치 방법**:
  - Pico CSS는 웹 페이지를 보기 좋게 만들어주는 작은 양의 CSS입니다.
  - 설치를 위해 CDN 링크를 복사하여 HTML의 `<head>` 부분에 붙여넣습니다.

- **레이아웃 기초**:
  - Pico CSS는 몇 가지 간단한 레이아웃 기술을 제공합니다.
  - **Container**: 요소를 중앙에 배치하려면, `<main class="container">` 안에 내용을 넣습니다.
    ```html
    <body>
      <main class="container">
        <!-- 내용 -->
      </main>
    </body>
    ```

- **테이블 사용 방법**:
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

- **테이블 추가 스타일링**:
  - **가로 줄 추가**: `<table role="grid">`를 사용하여 테이블에 가로 줄을 추가할 수 있습니다.
  - **가로 스크롤 추가**: `<figure>` 태그 안에 테이블을 넣어 가로 스크롤을 추가할 수 있습니다.


### Flask에서 데이터베이스(DB) 만들기

- **DB 생성 위치**:
  - DB는 함수 밖에서 생성되어야 합니다. 이렇게 하면 서버가 작동하는 동안에만 DB가 유지됩니다.

- **Search 함수에서 DB 사용**:
  - 사용자가 입력한 키워드로 DB를 검색하여 이미 저장된 결과가 있는지 확인합니다.
  - DB에 키워드에 해당하는 데이터가 없다면, 새로 데이터를 추출하고 DB에 저장합니다.
  ```python
  # DB 생성 (예시)
  db = {}

  # Search 함수
  def search_function():
      keyword = request.args.get("keyword")
      if keyword in db:
          jobs = db[keyword]
      else:
          indeed_jobs = extract_indeed_jobs(keyword)
          wwr_jobs = extract_wwr_jobs(keyword)
          jobs = indeed_jobs + wwr_jobs
          db[keyword] = jobs
      return render_template("your_template.html", jobs=jobs)
