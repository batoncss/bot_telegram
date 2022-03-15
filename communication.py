from requests import get

def weather(city_):
    if city_ == "Spb":
        site = "https://world-weather.ru/pogoda/russia/saint_petersburg/"
        city_find = "|Санкт-Петербург|"
    elif city_ == "Omsk":
        site = "https://world-weather.ru/pogoda/russia/omsk/"
        city_find = "|Омск|"
    else:
        return "Ваш город недоступен"
    page = get(site)
    data = page.text
    find_start_false = data.find(city_find)
    find_start = data.find("|", find_start_false + 1, )
    find_finish = data.find("|", find_start + 1, )
    number = ""
    for i in range(find_start + 1, find_finish):
        number += data[i]
    return number

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
        text = f'Погода в СПб: {weather("Spb")} градуса по Цельсию'
    else:
        text = 0
    return text