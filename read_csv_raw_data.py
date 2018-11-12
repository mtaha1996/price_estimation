import pandas as pd
import os


class ReadCsvData:
    def __init__(self, path_raw_csv, header=None):
        # path to .csv file that contains the data
        path = path_raw_csv

        # read the csv file from the
        self.df = pd.read_csv(path, header=header)

    def add_column_header(self, header):

        # if there is no headers for your columns you can add a list of headers

        # header = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors",
        # "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight",
        # "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio",
        # "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

        self.df.columns = header

    def show_n_first(self, number_of_lines):
        print(self.df.head(number_of_lines))

    def __str__(self):
        self.df.head()

    def save_as_csv(self, path, file_name):
        des = os.path.join(path, file_name)
        self.df.to_csv(des)

    def save_as_json(self, path, file_name):
        des = os.path.join(path, file_name)
        self.df.to_json(des)

