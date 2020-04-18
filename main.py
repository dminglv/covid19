from libs.apis import getCountryInfo, getCountries, getCountriesNames
from libs.charts import visualize


def main():
    arr = []

    number = 10

    # Get top 10 countries
    countries = getCountries(number)
    countries_names = getCountriesNames(number)

    for i in range(len(countries)):
        country = countries[i]
        country_names = countries_names[i]
        country_info = getCountryInfo(country)

        d = {
            'country': country_names,
            'info': country_info
        }

        arr.append(d)

    visualize(arr)


if __name__ == "__main__":
    main()
