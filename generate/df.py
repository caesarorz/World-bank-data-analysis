import pandas as pd
import numpy as np

class GenerateDataFrame:
    """Generate most common dataframes"""

    def __init__(self):
        self.df_ = []

    def set_df_one_indicator(self, dict):
        self.df_= pd.DataFrame.from_dict(data=dict)

    def get_df_one_indicator(self):
        return self.df_

    def merge_df_multiple(self):
        pass

    def transform_df(self):
        pass