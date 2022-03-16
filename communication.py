from requests import get
from weather import text_for_weather
from money import text_for_money

def news():
    page = get('https://vc.ru/popular')
    data = page.text
    find_start = data.find('Статьи редакции')
    url_start = data.find('https://vc.ru/', find_start)
    url_finish = data.find('"', url_start)
    number = ""
    for i in range(url_start, url_finish):
        number += data[i]
    return number


def text_for_answer(text):
    if text == '/news':
        text = news()
    elif text == 'кек':
        text = 'чебурек'
    elif text == '/weather':
        text = text_for_weather()
    elif text == '/money':
        text = text_for_money()
    else:
        text = 0
    return text