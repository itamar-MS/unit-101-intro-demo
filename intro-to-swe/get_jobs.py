import requests
from bs4 import BeautifulSoup
import json
from colorama import init as colorama_init
from colorama import Fore


print_table_row = lambda x, y, z: print(f"{Fore.RED} {x:<70.70} | {Fore.BLUE} {y:<40.40} | {Fore.GREEN} {z}")


def extract_job_data(url):
    res = requests.get(url)
    parser = BeautifulSoup(res.text, 'html.parser')

    # Extract title, company and location
    title = parser.find('div', {'data-test': 'job-title'}).text
    company = parser.find('div', {'data-test': 'employer-name'}).text
    location = parser.find('span', {'data-test': 'location'}).text

    print_table_row(title, company, location)


def main():
    colorama_init()
    keyword = input("Enter job title: ")

    # Get the jobs from Glassdoor
    print(f"{Fore.RED} Getting jobs for {keyword} from Glassdoor...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    res = requests.get("https://www.glassdoor.com/Job/jobs.htm?sc.keyword=" + keyword, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    scripts = soup.findAll('script')
    jobs = json.loads(scripts[2].text)['itemListElement']

    print(f"\n{Fore.RED} Found jobs!")
    print("-"*150)
    print_table_row('Job Title', 'Company', 'Location')
    print("-"*150)

    # Get the information for each job
    for job in jobs:
        try:
            extract_job_data(job['url'])
        except Exception:
            pass


if __name__ == "__main__":
    main()
