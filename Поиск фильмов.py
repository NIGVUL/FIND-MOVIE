import requests
from bs4 import BeautifulSoup
import webbrowser
import easygui


nameFilm = '+'.join( easygui.enterbox('Введите название фильма: ', 'Поиск фильма').split() )

URL = f'https://www.kinopoisk.ru/index.php?kp_query={nameFilm}'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
res = requests.get(URL, HEADERS)
soup = BeautifulSoup(res.text, 'html.parser')
lst = soup.find('div', class_='element most_wanted').find('a', class_='js-serp-metrika').attrs

neededUrl = f'https://www.ggkinopoisk.ru/{lst["data-type"]}/{lst["data-id"]}/'
webbrowser.open(neededUrl, new=2)
