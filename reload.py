import os
from pathlib import Path
import json
import random


def get_file_list(path, file_list=[]):
    ans = os.listdir(path)
    for file in ans:
        if os.path.isdir(path/file):
            get_file_list(path/file, file_list)
        else:
            if ".git" not in str(path/file) and "README.md" not in str(path/file) and "reload.py" not in str(path/file) and "info.json" not in str(path/file):
                file_list.append(str(path/file).replace("\\", "/"))
    return file_list


def main():
    files = get_file_list(Path("./"))
    tar = []
    ids = random.sample(range(1000000000000, 10000000000000), len(files))
    for i in range(len(files)):
        tar.append({
            "id": ids[i],
            "image": "https://cdn.jsdelivr.net/gh/TinyBear2222/ImageHost@main/"+files[i],
            "loading": False,
            "createTime": "2000-01-01"
        })
    with open("info.json", "w") as f:
        f.write(json.dumps(tar))


if __name__ == "__main__":
    main()
