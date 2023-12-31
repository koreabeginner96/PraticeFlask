from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
browser = webdriver.Chrome(options=options)

def get_page_count(keyword):

    base_url = "https://kr.indeed.com/jobs"
    browser.get(f"{base_url}?q={keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find('nav', class_='css-jbuxu0 ecydgvn0')
    if pagination == None:
        return 1
    pages = pagination.find_all('div', recursive=False)
    length = len(pages)
    if length == None:
        return 1
    return length

def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    result = []
    for page in range(pages):
        base_url = "https://kr.indeed.com/jobs"
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        print("Requesting",final_url)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        browser.get(f"{base_url}?q={keyword}&start={page*10}")

        
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
                    'company' : company.string.replace(","," "),
                    'location' : location.string.replace(","," "),
                    'position' : title,
                }
                result.append(job_data)
    return result
