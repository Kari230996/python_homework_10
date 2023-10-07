'''
📌 Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра.
'''

# ДЗ 8 задача 2


import os
import json
import csv
import pickle


class DirectoryProcessor:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.results = []

    def get_dir_size(self, dir_path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(dir_path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)

        return total_size

    def save_dir_contents(self):

        def process_dir(directory):
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                item_type = "file" if os.path.isfile(
                    item_path) else "directory"

                if item_type == "file":
                    item_size = os.path.getsize(item_path)

                else:
                    item_size = self.get_dir_size(item_size)

                self.results.append({
                    "name": item,
                    "path": item_path,
                    "type": item_type,
                    "parents_directory": directory
                })

                if os.path.isdir(item_path):
                    process_dir(item_path)

        process_dir(self.input_dir)

        # Сохраняем результаты в JSON

        json_file_path = os.path.join(output_dir, "dir_contents.json")

        with open(json_file_path, 'w') as json_file:
            json.dump(self.results, json_file, indent=4)

        # Сохраняем результаты в CSV

        csv_file_path = os.path.join(output_dir, "dir_contents.csv")

        with open(csv_file_path, 'w', newline='') as csv_file:
            fieldnames = ['name', 'path', 'type', 'parent_directory']

            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(self.results)

        # Сохраняем результаты в Pickle

        pickle_file_path = os.path.join(output_dir, "dir_content.pkl")

        with open(pickle_file_path, 'wb') as pickle_file:
            pickle.dump(self.results, pickle_file)


if __name__ == "__main__":
    input_dir = "/python_homework_10"
    output_dir = "/10"

    directory_processor = DirectoryProcessor(input_dir, output_dir)
    directory_processor.save_dir_contents()
