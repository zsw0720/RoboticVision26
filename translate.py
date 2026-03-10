import json
import re
import os

file_path = '直接拼接task1+task2.ipynb'

if not os.path.exists(file_path):
    print(f"File not found: {os.path.abspath(file_path)}")
else:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    def find_chinese(obj):
        found = []
        if isinstance(obj, str):
            if re.search(r'[\u4e00-\u9fff]', obj):
                found.append(obj)
        elif isinstance(obj, list):
            for item in obj:
                found.extend(find_chinese(item))
        elif isinstance(obj, dict):
            for k, v in obj.items():
                found.extend(find_chinese(v))
        return found

    print("Chinese strings found:")
    for s in find_chinese(data):
        print(repr(s))
