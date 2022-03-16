from requests import get


def long_polling(token, update_id):
    while True:
        result = get(f'https://api.telegram.org/bot{token}/getUpdates?timeout=2&offset={update_id}').json()['result']
        if result != []:
            update_id = result[0]['update_id'] + 1
            return result, update_id


def answer(token, chat_id, text):
    if text != 0:
        if text[:16] == "https://topmemas":  # если в тексте ссылка на картинку
            return get(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&photo={text}').text
        else:
            return get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}').json()
    else:
        return None
