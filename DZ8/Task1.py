# 2.Напишите функцию, которая получает на вход директорию и рекурсивно обходит
# её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом
# всех вложенных файлов и директорий.

import os
import json
import csv
import pickle
from DZ.DZ8.getsz import get_size


def directory_walker(dir_path):
    results = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            full_path = os.path.join(root, name)
            results.append({"parent_directory": root,
                            "isFile": True,
                            "name": name,
                            "size_bytes": os.path.getsize(full_path)})

        for name in dirs:
            full_path = os.path.join(root, name)
            results.append({"parent_directory": root,
                            "isFile": False,
                            "name": name,
                            "size_bytes": get_size(full_path)})

    with open("./OutputFiles/json.json", "w") as json_file:
        json.dump(results, json_file)

    with open("./OutputFiles/csv.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    with open("./OutputFiles/pickle.pickle", "wb") as pickle_file:
        pickle.dump(results, pickle_file)
