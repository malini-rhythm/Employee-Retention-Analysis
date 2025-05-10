import pandas as pd
import time
from ydata_profiling import ProfileReport


class InputOptimization:
    """Input Optimization Functions"""

    def generate_profile_report(self, df, path, title):
        profile = ProfileReport(df, title=title, html = {'style':{'full_width': True}})

        epoch = round(time.time() * 1000)
        report_name = path + '/profile_' + title + str(epoch) + '.html'
        profile.to_file(output_file=report_name)

    def validate_types(self, df:pd.DataFrame):
        """Tabulate Data Types and Unique Values"""
        columns = df.columns
        col_types = []

        for column in columns:
            data_type = 'object'

            if df[column].nunique() > 2:
                if df[column].dtype == 'int64' or df[column].dtype == 'float64':
                    data_type = 'numerical'
                else:
                    data_type = 'categorical'
            elif df[column].nunique() > 1:
                data_type = 'binary'
            else:
                data_type = 'constant'

            # Total Unique Values
            nuniques = df[column].nunique()

            col_types.append([column, data_type, nuniques])

        df = pd.DataFrame(col_types)
        df.columns = ['Column', 'Data Type', 'Unique Values']
        df = df.sort_values(by='Unique Values', ascending=False)
        return df

