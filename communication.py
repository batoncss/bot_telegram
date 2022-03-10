from requests import get


def news():
    page = get('https://vc.ru')
    data = page.text
    find_start = data.find('<div class="l-inline">')
    find_finish = data.find('class="n', find_start)
    number = ""
    for i in range(find_start + 40, find_finish - 13):
        number += data[i]
    return number


def text_for_answer(text):
    if text == '/news':
        text = news()
    else:
        text = 0
    return text