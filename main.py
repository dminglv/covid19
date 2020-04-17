from libs.apis import getCountryInfo, getCountries, getCountriesNames
from libs.graphs import visualize

# Get top 10 countries
countries = getCountries(10)
countries_names = getCountriesNames()
mass = []

for i in range(len(countries)):
    country = countries[i]
    country_names = countries_names[i]
    country_info = getCountryInfo(country)
    dict = {
        'country': country_names,
        'info': country_info
    }
    mass.append(dict)

visualize(mass)
