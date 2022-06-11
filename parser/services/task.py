from requests import request, session
from .google_search import search
import requests_html

session = requests_html.HTMLSession()

def main():
    # data = []
    # for v in search('Automotive workshops', num_results=100):
    #     data.append(v)
    r = session.get(url='https://invilso.pp.ua/')
    r.html.render()
    with open('file.html', encoding='utf-8', mode='w+') as f:
        f.write(r.text)
    return r.text
