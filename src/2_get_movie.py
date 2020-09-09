from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.themoviedb.org/person/6384-keanu-reeves')
soup = BeautifulSoup(page.text, 'html.parser')
if page.status_code == 200:
    div = soup.find_all(class_="credit_group")
