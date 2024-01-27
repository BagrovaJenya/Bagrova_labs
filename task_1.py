# TODO решите задачу
import json
def task() -> float:
    file_path = "input.json"
    with open(file_path) as file:
        data = json.load(file)

    return round(sum([i["score"] * i["weight"] for i in data]), 3)

print(task())
