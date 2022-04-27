import pandas as pd
import numpy as np


def create_df(data, sep):

    df = pd.read_csv(data, sep=sep)

    # ensure evrything is numeric in data
    def is_numeric(string):    
        try:
            float(string)      
            val = float(string)
        except ValueError:
            val = np.nan
        return val
    
    numeric_df = pd.DataFrame(columns=df.columns.to_list())
    
    for i in range(len(df.columns)):
        numeric_df[df.columns[i]] = df[df.columns[i]].apply(is_numeric)

    df = numeric_df.dropna()

    return df

def filter_df_per_direction(df, direction, direction_step):
    """filter the df according to direction
    It centers the df around the direction +/- 0.5*direction step
    """
    
    if direction == 0:
        df_filter = df[(df[df.columns[1]]>= 360 - 0.5*direction_step) |
                       (df[df.columns[1]]< 0 + 0.5*direction_step)]
    else:
        df_filter = df[(df[df.columns[1]]>= direction - 0.5*direction_step) &
                       (df[df.columns[1]]< direction + 0.5*direction_step)]
    
    return df_filter

def create_distibution(df, direction_step, density=False):
    
    wind_speed_range = np.arange(0, 40, 1)

    wind_speed_ticks = ["[{}-{}[".format(i, i + 1) for i in wind_speed_range[:-1]]
    wind_direction_ticks = ["[0:{}-{}[".format(360 - direction_step/2, 0 + direction_step/2)]
    _dir = 22.5
    while _dir < 360:
        wind_direction_ticks.append("[{}:{}-{}[".format(_dir, _dir - 0.5*direction_step, _dir + 0.5*direction_step))
        _dir += direction_step
       

    histo2D = pd.DataFrame(data=None, index=wind_speed_ticks, columns=wind_direction_ticks)
    k = 0
    for _dir in np.arange(0, 360, direction_step):
        df_filter = filter_df_per_direction(df, _dir, direction_step)
        histo2D.iloc[:,k] = np.histogram(df_filter[df.columns[0]], bins=wind_speed_range)[0]
        k += 1
    
    if density:
        # have the distrib in pourcentage
        histo2D = histo2D.apply(lambda x: x/histo2D.sum().sum()).dropna(axis=1)

    return histo2D
