from read_csv_raw_data import ReadCsvData

path_raw = "data/imports-85.data"

path_to_save = "results"

header = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors",
          "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight",
          "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio",
          "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

myAnalyse = ReadCsvData(path_raw)
myAnalyse.add_column_header(header)
myAnalyse.show_n_first(3)
#myAnalyse.save_as_csv(path_to_save, "vid_5.csv")
#myAnalyse.save_as_json(path_to_save, "vid_5.json")
