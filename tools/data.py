import os
import csv
import pandas as pd

def write_row(path, file_name, data):
    with open(path+file_name, 'a') as archive:
        writer = csv.writer(archive)
        writer.writerow(data)


def export_to_csv(path, file_name, data_frame):
    data_frame.to_csv(path+file_name, index=False)


def has_file(path, file_name):
    return os.path.isfile(path+file_name)


def get_data_frame(file_name):
    return pd.read_csv("./results/"+file_name, encoding='utf-8')