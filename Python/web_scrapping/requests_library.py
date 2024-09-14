import time

from bs4 import BeautifulSoup
import requests
# from timesjobs.com, get the most recent job posting for a python related job

print('Enter a skill that you are unfamiliar with')
unfamiliar_skill = input('> ')
print('Filtering out unfamiliar skill')


def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?'
                             'searchType=personalizedSearch&from=submit&searchTextSrc=&'
                             'searchTextText=&txtKeywords=python&txtLocation=').text
    # converts the html text into text format
    soup = BeautifulSoup(html_text, 'lxml')
    jobs_category = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')  # you can also use jobs_category.find
    for index, job in enumerate(jobs_category):
        # enumerate allows you to iterate over the index of the job lists and its contents
        publish_date = job.find('span', class_='sim-posted').text
        # finds the text that shows how long ago it was posted

        if 'day' or 'days' in publish_date:  # filters for posts with this text
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')  # h3 is a heading in l1
            # replace function removes whitespaces
            skills = job.find('span', class_='srp-skills').text
            more_info = job.header.h2.a['href']
            # adding the href in brackets ensures that only the attribute (link) is displayed
            # the rest of the information from <a href> is left out
            if unfamiliar_skill not in skills:
                with open(f'job_posts/{index}.txt', 'w') as f:
                    # the contents of the scraping are written in files
                    f.write(f'Company : {company_name.strip()}\n')  # strip removes unnecessary whitespaces
                    f.write(f'Skills required : {skills.strip()}\n')
                    f.write(f'More info : {more_info}\n')
                print(f'File saved in {index}\n')


if __name__ == '__main__':
    while True:
        find_jobs()
        time.sleep(600)
        # the program refreshes every 600 seconds to check for a new job
