import configparser


def data():
    config = configparser.ConfigParser()
    config.read("settings.ini")
    token = config['Bot']['token']
    return token