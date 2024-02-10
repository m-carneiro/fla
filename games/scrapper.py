from bs4 import BeautifulSoup
import requests as req

url = "https://www.placardefutebol.com.br/time/flamengo/proximos-jogos"

def get_html(url):
    response = req.get(url)
    return response.text
  
def get_matches() -> list[list[str]]:
    info = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    matches = soup.find_all('div', class_='match__lg_card')
    for match in matches:
        result = match.text.split('\n')  
        info.append(result)  
    
    for i in range(len(info)):
        info[i] = list(filter(lambda x: x != '', info[i]))
    # deepcode ignore useCompehensions: <please specify a reason of ignoring this>
    
    return info
