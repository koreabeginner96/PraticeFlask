from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs



keyword =input("what do u want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr =extract_wwr_jobs(keyword)

jobs = indeed + wwr

#csv 파일만들기
file = open(f"{keyword}.csv","w",encoding="utf-8")
#파일 헤더 \n 필수!
file.write("Position,Company,Location,URL \n")
#합치려면 같은 key를 써야한다. 필요한거 다 작성후 \n
for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()



#get_page_count 파이썬 검색 첫페이지 가고 다음 페이지 있는 지 확인 하기-> pagination 확인해서 카운트 ->
#페이지만큼 카운팅하여 정보 가져오기
