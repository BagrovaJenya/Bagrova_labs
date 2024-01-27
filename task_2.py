# TODO импортировать необходимые молули

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME) as file:
        lines = [line for line in csv.DictReader(file)]
        json_file = open(OUTPUT_FILENAME, "w")
        json.dump(lines, json_file, indent=4)
        json_file.close()

    # TODO считать содержимое csv файла
    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
