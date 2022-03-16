from weather import text_for_weather
from money import text_for_money
from joke import text_for_joke
from memes import url_with_memes
from news import text_for_news


def text_for_answer(text):
    if text == '/news':
        text = text_for_news()
    elif text == 'кек':
        text = 'чебурек'
    elif text == '/weather':
        text = text_for_weather()
    elif text == '/money':
        text = text_for_money()
    elif text == '/joke':
        text = text_for_joke()
    elif text == '/memes':
        text = url_with_memes()
    else:
        text = 0
    return text
