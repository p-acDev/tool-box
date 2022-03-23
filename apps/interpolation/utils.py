import pandas as pd
import numpy as np

def do_interpolation(data, separator=";"):

    df = pd.read_csv(data, sep=separator)

    x, y = df['x'], df['y']

    # to be chosen by user
    x_new = np.arange(0, 360, 30)

    y_new = np.interp(x_new, x, y)


    df_interp = pd.DataFrame()
    df_interp["x"] = x_new
    df_interp["y"] = y_new


    return df, df_interp