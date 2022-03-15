from requests import get


def news():
    page = get('https://vc.ru')
    data = page.text
    find_start = data.find('<div class="content-header__info">')
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