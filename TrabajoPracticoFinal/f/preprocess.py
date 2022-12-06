import pandas as pd 

def transformar_dt(df):
    df.loc[:, "dt"] = \
        pd.to_datetime(df["dt"])
    return df


def anio(df):
    df.loc[:, "anio"] = \
        pd.DatetimeIndex(df['dt']).year
    return df