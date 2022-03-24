from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as csvfile:
        file_reader = csv.DictReader(csvfile)
        list_all_rows = []
        for row in file_reader:
            list_all_rows.append(row)
    return list_all_rows
