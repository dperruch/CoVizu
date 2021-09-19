"""

DavidPerruchoud @ Aktiia SA (created on 18/09/2021)
"""
from datetime import datetime
from io import StringIO
import matplotlib.pyplot as plt
from requests import get
import pandas as pd
import seaborn as sns

from csv_loader import CsvLoader


def plot_weekly_death_by_age():
    sns.set_theme('notebook')

    df = CsvLoader.load_csv_dataset(('weekly', 'byAge', 'death'), weekly_dt_columns='datum')
    df = df[df.geoRegion == 'CH'].copy()

    df = df[df.altersklasse_covid19 != 'Unbekannt'].copy()
    df['age_approx'] = df.altersklasse_covid19.replace(
        {'0 - 9': 5,
         '10 - 19': 15,
         '20 - 29': 25,
         '30 - 39': 35,
         '40 - 49': 45,
         '50 - 59': 55,
         '60 - 69': 65,
         '70 - 79': 75,
         '80+': 85})
    plt.figure(figsize=(14, 8))
    sns.lineplot(data=df, x='datum', y='entries', hue='altersklasse_covid19', lw=3)
    plt.yscale('log')
    plt.ylabel("Number of deaths per week")
    plt.title("Swiss death across age group")

    plt.figure(figsize=(14, 8))
    df_combined = df.copy()
    df_combined = df_combined[['datum', 'altersklasse_covid19', 'entries']]
    df_combined.altersklasse_covid19 = df_combined.altersklasse_covid19.replace({
        '0 - 9': '<50',
        '10 - 19': '<50',
        '20 - 29': '<50',
        '30 - 39': '<50',
        '40 - 49': '<50'
    })

    grouped = df_combined.groupby(['datum', 'altersklasse_covid19'])
    df_combined = grouped.sum()
    df_combined.reset_index(drop=False, inplace=True)
    sns.lineplot(data=df_combined, x='datum', y='entries', hue='altersklasse_covid19', lw=3)
    plt.yscale('log')
    plt.ylabel("Number of deaths per week")
    plt.title("Swiss death across age group")



    grouped = df.groupby('datum')
    aggr = grouped.agg(lambda dataf: dataf.entries.multiply(dataf.age_approx).sum() / dataf.entries.sum())['entries']

    plt.figure()
    plt.plot(aggr)
    plt.show()
    print()


if __name__ == '__main__':
    plot_weekly_death_by_age()