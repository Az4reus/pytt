from typing import List


def read_file(path) -> str:
    with open(path) as f:
        ret = f.read()
        return str(ret)


def read_file_lines(path) -> List[str]:
    with open(path) as f:
        return f.readlines()


def write_file(path, content) -> None:
    with open(path, 'w') as f:
        f.write(content)
