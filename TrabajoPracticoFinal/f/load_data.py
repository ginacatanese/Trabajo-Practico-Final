import pandas as pd
import os

def normalize_name(filename):
    return filename.replace("GlobalLandTemperaturesBy", "").replace(".csv", "")

def load_all_data(path):
    ''' read all datasets in folder and usea as name'''
    files = [f for f in os.listdir(path) if f.endswith(".csv")]
    data = {normalize_name(filename): pd.read_csv(f"{path}/{filename}").reset_index() for filename in files}
    return data


