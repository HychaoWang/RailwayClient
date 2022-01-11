import requests
from Simulator import *


def url_check(url):
    if "http" not in url:
        url = "http://" + url
    return url


def connect(url):
    url = url_check(url)
    get = requests.get(url + '/check/')
    return get.status_code


def signup(url, username, password):
    dict = {"username": username, "password": password}

    response = requests.get(url + '/SignUp/', dict)
    return response.status_code


def login(url, username, password):
    dict = {"username": username, "password": password}
    response = requests.get(url + '/LogIn/', dict)
    print(response.text)
    return response.status_code


def send_speed(url, user, location, velocity):
    dict = {"User": user, "Location": location, "Velocity": velocity}
    response = requests.get(url + '/demo_predict/', dict)
    return response


def receive(response):
    text = response.text
    return text


def msg_parser(text):
    list = text.split(',', 1)
    return list


def hlt():
    print('hlt')


if __name__ == '__main__':

    run_state = 0
    hlt = 0
    # url = input()
    url = '192.168.0.106:5000'
    url = url_check(url)

    try:
        connect(url)
    except:
        print("connection error")

    username = 'lyc'
    password = '666'
    login(url, username, password)

    run_state = 1
    dict = get_data()
    for key in dict.keys():
        print(key, dict[key])
        response = send_speed(url, key, dict[key])
        text = receive(response)
        print(text)
        list = msg_parser(text)
        print(list)
        error = list[0]
        hlt = list[1]
        if hlt == 1:
            hlt()
