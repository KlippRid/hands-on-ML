# Helper functions for importing data
import os
import tarfile
import urllib
import pandas as pd

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_tar_file(data_url=HOUSING_URL, data_path=HOUSING_PATH, file_name="housing.tgz"):
    if not os.path.isdir(data_path):
        os.makedirs(data_path)
    tgz_path = os.path.join(data_path, file_name)
    urllib.request.urlretrieve(data_url, tgz_path)
    data_tgz = tarfile.open(tgz_path)
    data_tgz.extractall(path=data_path)
    data_tgz.close()

def load_csv_data(data_path=HOUSING_PATH, file_name="housing.csv"):
    csv_path = os.path.join(data_path, "housing.csv")
    return pd.read_csv(csv_path)