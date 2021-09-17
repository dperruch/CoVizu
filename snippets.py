from datetime import datetime, timedelta
from io import StringIO

import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from requests import get
import seaborn as sns

from ofsp_context import Context

if __name__ == '__main__':
    context = Context()
    df = pd.read_csv(StringIO(get(context.daily.get('death')).text),
                     parse_dates=['datum', ])
    print()
    #
    # ch = df[df.geoRegion == 'CH'].copy()
    # df = df[df.geoRegion.isin(['ZH', 'VS'])].copy()
    # plt.figure()
    # # plt.plot(ch.datum, ch.mean7d)
    # sns.lineplot(data=df, x='datum', y='mean7d', hue='geoRegion')
    # # plt.legend()
    # plt.show()



