from requests import get


def text_for_joke():
    page = get("https://www.anekdot.ru/random/anekdot/")
    data = page.text
    find_start = data.find('<div class="text">')
    find_finish = data.find('</div>', find_start)
    number = ""
    for i in range(find_start + 18, find_finish):
        if data[i] == "<":
            number += "\n"
        elif data[i] == "b" or data[i] == "r" or data[i] == ">":
            number += ""
        else:
            number += data[i]
    return number