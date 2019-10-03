from bs4 import BeautifulSoup
import requests
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

def get_info(url):
    req = requests.get(url)
    errorjornada = ['no data','no data','no data','no data','no data']

    soup = BeautifulSoup(req.text, 'html.parser')

    jornada_box = soup.find("div", attrs={'id':'jornada_numero'})
    try:
        numero_jornada, date = str(jornada_box).split('<br/>', 4)
    except:
        numero_jornada = "Horaris no publicats encara"
        date = "Horaris no publicats encara"

    data = []
    tabla_box = soup.find('div', attrs={'class':'resultados'})

    rows = tabla_box.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    del data[0]
    dataSQV = []
    for element in data:
        if len(element) > 3:
            if 'SANT QUIRZE' in str(element[0]) or 'SANT QUIRZE' in str(element[1]):
                dataSQV.append(element)

    for element in dataSQV:
        data.append(element)

    data = {
        'Local': element[0],
        'Visitant': element[1],
        'Dia': element[2],
        'Hora': element[3],
        'Lloc': element[4],

    }

    return data
