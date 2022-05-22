from Bot import long_polling, answer
from communication import text_for_answer
from error_handling import error_massage
import configuration

token = configuration.data()
update_id = 0
while True:
    try:
        result, update_id = long_polling(token, update_id)
        chat_id = result[0]['message']['chat']['id']
        text = result[0]['message']['text']
        data = answer(token, chat_id, text_for_answer(text))
    except:
        error_massage()
