from requests import get, post
from random import randint

token = '5200346527:AAGUHn9YPoD6eOuEVp1esWtqdD1snJa9exc'
chat_id = 1469994194


def url_with_memes():
    data = get('https://topmemas.top').text
    memes = []
    false_start = 0
    for i in range(10):
        start = data.find('https://topmemas.top/view.php?mem=', false_start)
        finish = data.find('}', start)
        picture = ""
        for j in range(start, finish):
            picture += data[j]
        picture = picture[38:]
        memes.append(picture)
        false_start = finish
    return f'https://topmemas.top/img/img/{memes[randint(0, 9)]}.jpg'

#
