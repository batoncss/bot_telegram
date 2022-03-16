from requests import get
from random import randint


def picture_with_memes():
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
