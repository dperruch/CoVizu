"""

DavidPerruchoud @ Aktiia SA (created on 18/09/2021)
"""
from datetime import datetime
from io import StringIO
import matplotlib.pyplot as plt
from requests import get
import pandas as pd
import seaborn as sns

from ofsp_context import Context


def plot_weekly_death_by_age():
    context = Context()
    df = pd.read_csv(StringIO(get(context.weekly.get('byAge').get('death')).text))
    df.datum = df.datum.apply(lambda i: datetime.strptime(str(i) + '0', "%Y%W%w"))
    df = df[df.geoRegion == 'CH'].copy()

    sns.lineplot(data=df, x='datum', y='entries', hue='altersklasse_covid19')
    plt.yscale('log')
    plt.show()
    print()


if __name__ == '__main__':
    plot_weekly_death_by_age()