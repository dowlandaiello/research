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
from sklearn.linear_model import LinearRegression

# Demonstrating the relationship between economy size, and gdp growth rate
countries = ["United States", "United Kingdom", "Japan", "China", "Vietnam", "India"]

# GDP growth and per capita for each country
country_data = {}

with open("le_data/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_1068887.csv") as f, open("le_data/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_1068945.csv") as f2:
    readers = [csv.reader(f), csv.reader(f2)]

    for i, (growth_line, per_capita_line)  in enumerate(zip(*readers)):
        if len(growth_line) <= 1:
            continue

        if growth_line[0] in countries:
            country_data[growth_line[0]] = {
                "gdp_growth_rate": growth_line[5:],
                "gdp_per_capita": per_capita_line[5:]
            }

plt.figure(figsize=(4, 3))

ax = plt.axes()

for country in country_data:
    data = country_data[country]

    ax.plot(data["gdp_per_capita"], data["gdp_growth_rate"], marker="", color="olive", linewidth=2, label=country)

ax.set_xlabel("GDP per capita")
ax.set_ylabel("GDP growth rate")

plt.savefig("PepoThink.png")