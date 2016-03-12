import json
from typing import List

from src.classes.project import Project
from src.classes.task import Task
from src.serialise import ARCHIVE_LOCATION
from src.utils import read_file_lines


def load_archive(path: str = ARCHIVE_LOCATION) -> List[Project]:
    lines = read_file_lines(path)
    return [reconstruct_project(l) for l in lines]


def reconstruct_project(json_str: str) -> Project:
    if json_str == "":
        return

    obj = json.loads(json_str)
    return Project(obj['title'], obj['pid'], reconstruct_tasks(obj['tasks']))


def reconstruct_tasks(raw_object) -> list:
    ret_list = []
    for item in raw_object:
        t = Task(item['title'], item['pid'], item['is_done'], item['is_hidden'])
        ret_list.append(t)

    return ret_list


def get_current_project(path=ARCHIVE_LOCATION) -> Project:
    try:
        with open(path) as f:
            first_line = f.readline()
            return reconstruct_project(first_line)
    except FileNotFoundError:
        return None
