import os
from list_sities import websites , websites_keys , headers
import requests
list = []
def requests_ru(url,i,nick):
    try:
        if requests.get(url,headers=headers).status_code == 404:
            print(f'[*] {i} : Страница не найдена!')
        if requests.get(url,headers=headers).status_code == 200:
            print(f'[*] {i} : {url}')
            if os.path.isfile(f'{nick}.txt'):
                os.remove(f'{nick}.txt')
            list.append(url)
    except Exception as e:
        print(f'[*] {i} : Ошибка')
def requests_en(url,i,nick):
    try:
        if requests.get(url,headers=headers).status_code == 404:
            print(f'[*] {i} : Page not found!')
        elif requests.get(url,headers=headers).status_code == 200:
            print(f'[*] {i} : {url}')
            if os.path.isfile(f'{nick}.txt'):
                os.remove(f'{nick}.txt')
            list.append(url)
    except Exception as e:
        print(f'[*] {i} : Error')

a=('''
+-+ +-+ +-+ 
| Nick-CHK |
+-+ +-+ +-+ 
''')
print(a)
lang=input('Choose a Language (ru/en): ').lower()
if lang == 'ru':
    nick = input('Введите ник:').lower()
    if nick == '':
        print('Пустое имя!')
    else:
        print('Процесс начался! Это может занять некоторое время.')
        for i in websites_keys:
            url1 = websites[i]+nick
            requests_ru(url1,i,nick)
        for b in list:
            with open (f'{nick}.txt','a+') as file:
                file.write(b +'\n')
        print(f'Процесс завершен! .txt сохранен , как "{nick}.txt" ')
elif lang == 'en':
    nick = input('Input Nickname:')
    if nick == '':
        print("This filed hasn't have a name!")
    else:
        print('Process has begun! This may take some time.')
        for i in websites_keys:
            url1 = websites[i] + nick
            requests_en(url1, i,nick)
        for b in list:
            with open (f'{nick}.txt','a+') as file:
                file.write(b +'\n')
        print(f'This process has finished! .txt file saves as "{nick}.txt" ')
else:
    print('Language not choose!')