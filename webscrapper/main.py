from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get("https://kr.indeed.com/jobs?q=python")

result = []
soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="css-zu9cdh eu4oa1w0")
jobs = job_list.find_all('li',recursive=False)

for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
        h2 = job.find("h2", class_= "jobTitle")
        anchor = job.select_one("a")
        title= anchor['aria-label']
        link = anchor['href']
        company = job.find("span", attrs={"data-testid":"company-name"})
        location = job.find("div", attrs={"data-testid":"text-location"})
        job_data={
            'link' : f"https://kr.indeed.com{link}",
            'company' : company.string,
            'location' : location.string,
            'position' : title
        }
        result.append(job_data)
for r in result:
    print(result,"\n///////\n")