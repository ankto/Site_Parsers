#https://www.creativeheads.net
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# Taken Response to web-site
def get_html(url):
    r = requests.get(url)
    return r.text

# Creating excel-file to receive data
def write_csv(data):
    with open('Creativeheads.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['Company name'],
                         data['Title'],
                         data['City'],
                         data['Country'],
                         data['Link of Source']))

def get_jobs_data(html):
    soup = BeautifulSoup(html,'lxml')

    jobs = soup.find('div', class_='jobs').find_all('div', class_='job')

    for job in jobs:
        # a Find job-title
        try:
            title = job.find('div', class_='job-content').find('h3').find('a').text
        except:
            title = ''
        # url Find job-link
        try:
            url = 'https://www.creativeheads.net' + job.find('div', class_='job-content').find('h3').find('a').get('href')
        except:
            url = ''
        # p Find Company name and the City
        try:
            company_name = job.find('div', class_='job-content').find('p').text.strip().split('-')[0]
        except:
            company_name = ''
        # p Find the City
        try:
            city = job.find('div', class_='job-content').find('p').text.strip().split('-')[1].split(',')[0]
        except:
            city = ''
        # Find Country/state
        try:
            country = job.find('div', class_='job-content').find('p').text.strip().split('-')[1].split(',')[1]
        except:
            country = ''

        data = {'Company name': company_name,
                'Title': title,
                'City': city,
                'Country': country,
                'Link of Source': url}
        #df = pd.DataFrame(data, data.items(), columns=['Company name', 'Title', 'City', 'Country', 'Link of Source'])
        #print(data['Company name'])
        write_csv(data)
def main():
    url = 'https://www.creativeheads.net'
    jobs_data = get_jobs_data(get_html(url))
    print(jobs_data)


if __name__=='__main__':
    main()