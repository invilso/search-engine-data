import imp
from .task import get_cityes_and_states
import bs4
import re

def modify_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    input = soup.find('input')
    text = input.get('value')
    count_states = 0
    count_cityes = 0
    cityes_and_states = get_cityes_and_states()
    states = False
    cityes = False
    for state in cityes_and_states:
        count_states += 1
        if state in text:
            states = True
            break
        for city in cityes_and_states[state]: 
            count_cityes += 1
            if city in text:
                cityes = True
                break
            
    count_all_states = 0
    count_all_cityes = 0
    for state in cityes_and_states:
        count_all_states+=1
        count_all_cityes+=len(cityes_and_states[state])
    text2 = ''
    if states:
        text2 = f'MODE-2: Parse cityes {count_states} out of {count_all_states} //Left: {count_all_states-count_states}'
    elif cityes:
        text2 = f'MODE-1: Parse cityes {count_cityes} out of {count_all_cityes} //Left: {count_all_cityes-count_cityes}'
    else:
        text2 = 'MODE-0: Don`t parse cityes and states.'
        
    return re.sub(text, f'{text} [[{text2}]]', html)
    
    

def get_html():
    get_cityes_and_states
    with open('file.html') as f:
        html = f.read()
    html = f'{modify_html(html)}'
    return html