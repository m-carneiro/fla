from bs4 import BeautifulSoup
from utils import create_html_file
import requests as req

url = "https://www.placardefutebol.com.br/time/flamengo"


def get_html(endpoint: str):
    response = req.get(url + endpoint)
    return response.text


def get_matches() -> list[list[str]]:
    info = []
    html = get_html("/proximos-jogos")
    soup = BeautifulSoup(html, 'html.parser')
    matches = soup.find_all('div', class_='match__lg_card')
    for match in matches:
        result = match.text.split('\n')
        info.append(result)

    for i in range(len(info)):
        info[i] = list(filter(lambda x: x != '', info[i]))
    # deepcode ignore useCompehensions: <please specify a reason of ignoring this>

    return info


def get_latest_matches() -> list[list[str]]:
    info = []
    html = get_html("/ultimos-jogos")
    # create_html_file("last-games", html)
    soup = BeautifulSoup(html, "html.parser")
    # for a in soup.find_all('a'):
    #     attributes = a.attrs
    #     print(f'Found this: {attributes['href']}')

    last_matches = soup.find_all('a', class_='match__lg')
    for match in last_matches:
        result = match.text.split('\n')
        info.append(result)

    for i in range(len(info)):
        info[i] = list(filter(lambda x: x != '', info[i]))

    return info

