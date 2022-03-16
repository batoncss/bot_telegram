from requests import get


def text_for_news():
    page = get('https://vc.ru/popular')
    data = page.text
    find_start = data.find('Статьи редакции')
    url_start = data.find('https://vc.ru/', find_start)
    url_finish = data.find('"', url_start)
    number = ""
    for i in range(url_start, url_finish):
        number += data[i]
    return number
