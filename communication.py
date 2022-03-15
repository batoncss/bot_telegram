from requests import get


def news():
    page = get('https://vc.ru/popular')
    data = page.text
    print(data)
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
    else:
        text = 0
    return text