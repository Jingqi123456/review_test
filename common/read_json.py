import json
import os.path

import config


def read_json(file_name):
    file_path = os.path.join(config.DATA_PATH, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        json_list = []
        json_info = json.load(f)
        for i in json_info:
            json_list.append(tuple(i.values()))
        return json_list


if __name__ == "__main__":
    print(read_json("login_data.json"))
