from list_sities import websites , websites_keys , headers
import requests
def requests_ru(url,i):
    try:
        if requests.get(url,headers=headers).status_code == 404:
            print(f'[*] {i} : Страница не найдена!')
        if requests.get(url,headers=headers).status_code == 200:
            print(f'[*] {i} : {url}')
    except Exception as e:
        print(f'[*] {i} : Ошибка')
def requests_en(url,i):
    try:
        if requests.get(url,headers=headers).status_code == 404:
            print(f'[*] {i} : Page not found!')
        if requests.get(url,headers=headers).status_code == 200:
            print(f'[*] {i} : {url}')
    except Exception as e:
        print(f'[*] {i} : Error')

a=('''
+-+ +-+ +-+ 
| Nick-CHK |
+-+ +-+ +-+ 
''')
print(a)
lang=input('Choose a Language (ru/en): ')
if lang == 'ru':
    nick = input('Введите ник:')
    if nick == '':
        print('Пустое имя!')
    else:
        for i in websites_keys:
            url1 = websites[i]+nick
            requests_ru(url1,i)
elif lang == 'en':
    nick = input('Input Nickname:')
    if nick == '':
        print('Пустое имя!')
    else:
        for i in websites_keys:
            url1 = websites[i] + nick
            requests_en(url1, i)
else:
    print('Language not choose!')