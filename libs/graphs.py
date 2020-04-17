import matplotlib as mpl
import matplotlib.pyplot as plt
import random


def visualize(data):
    fig = plt.figure(figsize=(15, 15), dpi=300)
    mpl.rcParams.update({'font.size': 8})
    for i in range(len(data)):
        country = data[i]['country']
        dates = []
        cases = []
        for j in range(len(data[i]['info'])):
            dates.append(data[i]['info'][j]['date'])
            cases.append(data[i]['info'][j]['cases'])

        plt.title('Charts of cases by top ' + str(len(data)) + ' countries')
        plt.xlabel('Date')
        plt.ylabel('Number of cases')

        plt.text(dates[-1], cases[-1], str(cases[-1]))

        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        plt.plot(dates, cases, color=color,
                 label=country)

    plt.legend(loc='upper left')
    fig.savefig('result.png')
