import requests
from datetime import datetime
from operator import itemgetter


def from_utc(utcTime, fmt="%Y-%m-%dT%H:%M:%SZ"):
    return datetime.strptime(utcTime, fmt)


def getCountries(numbers):
    countries = []
    json = requests.get('https://api.covid19api.com/summary').json()
    d = json['Countries']
    newlist = sorted(d, key=itemgetter('TotalConfirmed'), reverse=True)
    for i in range(numbers):
        countries.append(newlist[i]['Slug'])
    return countries


def getCountriesNames(numbers):
    countries = []
    json = requests.get('https://api.covid19api.com/summary').json()
    newlist = sorted(json['Countries'], key=itemgetter('TotalConfirmed'), reverse=True)
    for i in range(numbers):
        countries.append(newlist[i]['Country'])
    return countries


def getCountryInfo(country):
    json = requests.get('https://api.covid19api.com/total/country/' + country + '/status/confirmed').json()
    arr = []
    for i in range(0, len(json), 7):
        date = str(from_utc(json[i]['Date']).date()).split('-')
        date = date[2] + '.' + date[1] + '.' + date[0]

        if date != 'None':
            d = {
                'cases': json[i]['Cases'],
                'date': date
            }
            arr.append(d)
    return arr
