from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
#첫번째 폴더네임 . 파일네임 import function 네임
jobs =extract_wwr_jobs("python")
print(jobs)