from typing import List


def read_file(path) -> str:
    try:
        with open(path) as f:
            ret = f.read()
            return str(ret)
    except FileNotFoundError:
        return ""


def read_file_lines(path) -> List[str]:
    try:
        with open(path) as f:
            return f.readlines()
    except FileNotFoundError:
        return []


def write_file(path, content) -> None:
    with open(path, 'w') as f:
        f.write(content)
