import requests
from datetime import datetime
from operator import itemgetter


def from_utc(utcTime, fmt="%Y-%m-%dT%H:%M:%SZ"):
    return datetime.strptime(utcTime, fmt)


def getCountries(numbers):
    names = []
    json = requests.get('https://api.covid19api.com/summary').json()
    dict = json['Countries']
    newlist = sorted(dict, key=itemgetter('TotalConfirmed'), reverse=True)
    for i in range(numbers):
        names.append(newlist[i]['Slug'])
    return names


def getCountriesNames():
    names = []
    json = requests.get('https://api.covid19api.com/summary').json()
    dict = json['Countries']
    newlist = sorted(dict, key=itemgetter('TotalConfirmed'), reverse=True)
    for i in range(10):
        names.append(newlist[i]['Country'])
    return names


def getCountryInfo(country):
    json = requests.get('https://api.covid19api.com/total/country/' + country + '/status/confirmed').json()
    mass = []
    for i in range(0, len(json), 7):
        date = json[i]['Date']
        date = str(from_utc(date).date()).split('-')
        date = date[2] + '.' + date[1] + '.' + date[0]

        if date != 'None':
            dict = {
                'cases': json[i]['Cases'],
                'date': date
            }
            mass.append(dict)
    return mass
