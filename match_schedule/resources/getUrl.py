from resources.getInfo import get_info, remove_tags
from bs4 import BeautifulSoup
from dateutil.parser import parse
import datetime
import requests


def get_jornada(jornada):

    print(jornada)

    url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4050&jornada='+str(jornada)
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'html.parser')

    jornada_box = soup.find("div", attrs={'id':'jornada_numero'})
    numero_jornada, date = str(jornada_box).split('<br/>', 4)

    now = datetime.datetime.now()
    datetoday = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
    datetoday = str(datetoday)
    datetoday = parse(datetoday, dayfirst=True)

    date = str(date)
    date = remove_tags(date)
    date = parse(date, dayfirst=True)


    compare = date < datetoday

    if compare:
        jornada = jornada + 1
        return get_jornada(jornada)
    else:
        return jornada


def get_url(equipo):
    jornada = 1
    if equipo == 'infn':
        jornada = get_jornada(jornada)
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4050&jornada='+str(jornada)
        return get_info(url)
    elif equipo == 'infv':
        jornada = get_jornada(jornada)
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4120&jornada='+str(jornada)
        return get_info(url)
    elif equipo == 'infb':
        jornada = get_jornada(jornada)
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4120&jornada='+str(jornada)
        return get_info(url)
    elif equipo == 'infr':
        jornada = get_jornada(jornada)
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4114&jornada='+str(jornada)
        return get_info(url)
    elif equipo == 'cadn':
        jornada = get_jornada(jornada)
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4040&jornada='+str(jornada)
        return get_info(url)
    elif equipo == 'cadv':
        jornada = get_jornada(jornada)
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4094&jornada='+str(jornada)
        return get_info(url)
    elif equipo == 'cadb':
        jornada = get_jornada(jornada)
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4092&jornada='+str(jornada)
        return get_info(url)
    elif equipo == 'juvn':
        jornada = get_jornada(jornada)
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4038&jornada='+str(jornada)
        return get_info(url)
    elif equipo == 'juvv':
        jornada = get_jornada(jornada)
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4093&jornada='+str(jornada)
        return get_info(url)
    elif equipo == 'juvb':
        jornada = get_jornada(jornada)
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4091&jornada='+str(jornada)
        return get_info(url)
    else:
        jornada = get_jornada(jornada)
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4031&jornada='+str(jornada)
        return get_info(url)

def get_all_data():
    equipos = ['infn','infv','infr','cadn','cadv','cadb','juvn','juvv','juvb','sen']

    data = []
    for equipo in equipos:
        datateam = get_url(equipo)
        data.append(datateam)
    return data

def get_header():
    jornada = 1
    jornada = get_jornada(jornada)
    req = requests.get('http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4050&jornada='+str(jornada))
    errorjornada = ['no data','no data','no data','no data','no data']

    soup = BeautifulSoup(req.text, 'html.parser')

    header = soup.div.h2
    try:
        nombre_liga, categoria, fase, grupo, vuelta = str(header).split('<br/>', 4)
    except:
        data.append(errorjornada)

    jornada_box = soup.find("div", attrs={'id':'jornada_numero'})
    try:
        numero_jornada, date = str(jornada_box).split('<br/>', 4)
    except:
        numero_jornada = "Horaris no publicats encara"
        date = "Horaris no publicats encara"

    data = {
        'jornada': remove_tags(numero_jornada),
        'data': date
    }

    return data
