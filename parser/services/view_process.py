from ..models import QueryesPool
import bs4 
import re

def modify_html(html: str):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    input = soup.find('input')
    text = input.get('value')
    html2 = f'Left {QueryesPool.objects.all().count()} queryes'
    return re.sub(text, f'{text} [[ {html2} ]]', html)

def get_html():
    with open('file.html', 'r', encoding='utf-8') as f:
        return modify_html(html=f.read())