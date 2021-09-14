from datetime import datetime, timedelta
from io import StringIO

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from requests import get
import seaborn as sns

if __name__ == '__main__':
    temp = get('https://www.covid19.admin.ch/api/data/context')

    df = pd.read_csv(StringIO(get('https://www.covid19.admin.ch/api/data/20210914-7d21af7k/sources/COVID19Cases_geoRegion.csv').text),
                     parse_dates=['datum', ])

    ch = df[df.geoRegion == 'CH'].copy()
    df = df[df.geoRegion.isin(['ZH', 'VS'])].copy()
    plt.figure()
    # plt.plot(ch.datum, ch.mean7d)
    sns.lineplot(data=df, x='datum', y='mean7d', hue='geoRegion')
    # plt.legend()
    plt.show()



