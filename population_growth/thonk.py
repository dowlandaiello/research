'''
In order to address the manner of population growth in developed countries, one must first make the distinction between economies of scale, growing populations, stagnating populations,
and dying populations. Take, for example, Japan. Since 1974, the population of Japan has stagnated, experiencing a declining annual population growth rate, and, shortly after the Great
Recession, experienced its first year of population death--that is, more people have died in Japan in 2018 than immigrated to or were born in the same country. In this respect, Japan
opposes the United States. For most of its history, Japan has retained a radically nationalistic identity, and, as a result, has been weary of globalization since the establishment of
its first unifying shogunate. The United States, by contrast, has characterized itself as a melting pot of diverse cultures and peoples. Until recent times, the U.S. has enjoyed a largely
positive population growth rate, and, to this day, continues to grow with respect to its demography. Yet, both Japan and the United States bear a significant similarity: gdp growth rate.
In contrast to their differing population growth rates, both the United States and Japan have undergone relative stagnation with respect to GDP since the global recovery from the 2008
subprime mortgage crisis. One possible explanation for this convergence lies in the GDP per capita of these two countries: among its peers, the United States ranks first in GDP per capita,
at $62,794--40.1% higher than its most economically similar neighbors, the U.K. and Canada--, and, prior to the 2019 SARS-CoV-2 outbreak, experienced a u3 unemployment of 3.5%. Similarly,
prior to the enactment of public safety provisions in light of the ongoing outbreak, experienced an unemployment rate of 2.3% and a GDP per capita 104.1% higher than the average among its
geographic neighbors ($39,289.96). As such, the assertion can be made that, with respect to their geographic and economic neighbors, both the United States and Japan had achieved relative
economic stability at an equitable, and respectable rate for most people in the respective countries. In other words, both the United States and Japan have little room for exponential
growth. Exponential growth in this case refers to the sub-decadal GDP growth rates commonplace in developing or otherwise growing Asian economies. China, Vietnam, and India, for example,
experienced GDP growth rates of 6.6%, 7.1%, and 6.8%, respectively, but diverge radically with respect to the remaining economic and demographic indicators previously mentioned: India
experienced a population growth rate of only 1.0% in 2018, as did Vietnam, while China experienced an even lower growth rate of 0.5%. As a result of these measures, one might come to
inquire: why are Vietnam, China, and India growing so quickly if their populations aren’t significantly outpacing that of the United States and the U.K.? The answer lies in the fact that
China, India, and Vietnam have not yet reached economic stability, and have not yet become “economies of scale.” Among each of the aforementioned nations, China is the greatest in its GDP
per capita, at $9,770.85, but the lowest of the three in its GDP growth rate (i.e., 6.6%, in contrast to the 6.7% and 7.1% of India and Vietnam). As such, a logarithmic relationship between
the scale of a nation’s economy and its respective growth rate can be drawn.
'''

import csv
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.ticker import FormatStrFormatter, StrMethodFormatter
from sklearn.linear_model import LinearRegression

# Demonstrating the relationship between economy size, and gdp growth rate
countries = ["Vietnam", "China"]

datasets = ["GDP growth rate", "GDP per capita", "population growth rate"]

# GDP growth and per capita for each country
country_data = {}

def dataset():
    directory = "le_data"

    for name in os.listdir(directory):
        yield csv.reader(open(os.path.join(directory, name)))

readers = dataset()

for i, sources in enumerate(zip(*readers)):
    if len(sources[0]) <= 1:
        continue

    if sources[0][0] in countries:
        final_data = {}

        for j, source in enumerate(sources):
            data = source[5:-1]
            fixed_data = []

            for k, entry in enumerate(data):
                if entry == "":
                    if k == 0:
                        entry = float(next(filter(lambda x : x != "", data)))
                    else:
                        entry = fixed_data[k - 1]
                else:
                    entry = float(entry)

                fixed_data.append(entry)

            final_data[j] = fixed_data

        final_data["year"] = list(range(1960, 1960 + len(final_data[0])))

        country_data[sources[0][0]] = final_data

plt.figure(figsize=(20, 20))

subplots = [plt.subplots() * (len(country_data[countries[0]]) - 1)]

for country in country_data:
    data = country_data[country]

    for i, dataset in enumerate(data):
        ax = subplots[i][1]
        ax2 = ax.twinx()

        ax.plot(data["year"], dataset, marker="", linewidth=2, label=country)
        ax.set_xlabel("year")
        ax.set_ylabel(datasets[i])
        ax.yaxis.set_major_locator(plt.MaxNLocator(15))

        ax2.plot(data["year"], data[i - 1], marker="", linewidth=2, label=country)
        ax2.set_major_locator(plt.MaxNLocator(15))

plt.savefig("PepoThink.png")