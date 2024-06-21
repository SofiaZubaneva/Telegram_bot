import requests
from pprint import pprint

API_KEY = 'dict.1.1.20240619T132821Z.b557c116719b0ffc.13787d34aeb1d1174eb290f30ff3457ba54642a5'
BASE_URL = 'https://whitelabel.travel.yandex-net.ru/hotels/suggest'


def get_langs():
    response = requests.get(f'{BASE_URL}/getLangs', params={
        'key': API_KEY
    })
    return response


def lookup(lang, text, ui='ru'):
    response = requests.get(f'{BASE_URL}/lookup', params={
        'key': API_KEY,
        'lang': lang,
        'text': text,
        'ui': ui
    })
    return response


langs_response = get_langs()
if langs_response.status_code != 200:
    print('Не удалось получить список направлений перевода')
    exit(1)

langs = langs_response.json()
print('Выберите одно из доступных направлений перевода')
print(langs)
while (lang := input('Введите направление: ')) not in langs:
    print('Такого направления нет. Попробуйте ещё раз')

text = input('Введите слово или фразу для перевода: ')
lookup_response = lookup(lang, text)
if lookup_response.status_code != 200:
    print('Не удалось выполнить перевод:', lookup_response.text)
    exit(1)

pprint(lookup_response.json())