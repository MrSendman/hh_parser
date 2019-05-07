import requests
from bs4 import BeautifulSoup as bs


headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
          'user-agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}

base_url='https://ternopil.hh.ua/search/vacancy?text=manager&only_with_salary=false&clusters=true&area=133&enable_snippets=true&salary=&from=suggest_post'

def hh_parse(base_url, header):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-qa':'vacancy-serp__vacancy'})
        for div in divs:
            title = div.find('a', attrs={'data-qa':'vacancy-serp_vacancy-title'})
            print(title)
    else:
        print('ERROR')


hh_parse(base_url, headers)
