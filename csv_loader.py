"""

DavidPerruchoud @ Aktiia SA (created on 19/09/2021)
"""
from datetime import datetime
from io import StringIO
from requests import get

import pandas as pd

from ofsp_context import Context


class CsvLoader:
    def __init__(self):
        pass

    @staticmethod
    def load_csv_dataset(db_hierarchy: tuple,
                         daily_dt_columns: [list, str] = None,
                         weekly_dt_columns: [list, str] = None
                         ) -> pd.DataFrame:
        # deal with string as aruments for *dt_columns
        if isinstance(daily_dt_columns, str):
            daily_dt_columns = [daily_dt_columns, ]

        # get the context
        context = Context().get_csv_context(db_hierarchy)

        df = pd.read_csv(StringIO(get(context).text),
                         parse_dates=daily_dt_columns)

        # if daily_dt_columns is not None:
        #     if isinstance(daily_dt_columns, str):
        #         daily_dt_columns = (daily_dt_columns, )
        #         for col in daily_dt_columns:
        #             df[col] = df[col].apply()

        if weekly_dt_columns is not None:
            if isinstance(weekly_dt_columns, str):
                weekly_dt_columns = [weekly_dt_columns, ]
            for col in weekly_dt_columns:
                df[col] = df[col].apply(lambda i: datetime.strptime(str(i) + '0', "%Y%W%w"))

        return df


if __name__ == '__main__':
    CsvLoader.load_csv_dataset(('weekly', 'byAge', 'death'), weekly_dt_columns='datum')
