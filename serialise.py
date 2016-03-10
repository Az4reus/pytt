import json
from typing import List
from utils import write_file, read_file_lines
from classes.project import Project

ARCHIVE_LOCATION = "./.archive"


def replace_archive(projects: List[Project]) -> None:
    list_strings = [json_serialise(p) for p in projects]
    block = '\n'.join(list_strings)

    clean_archive(ARCHIVE_LOCATION)
    write_file(ARCHIVE_LOCATION, block)


def clean_archive(path: str) -> None:
    with open(path, 'w') as f:
        f.write("")


def json_serialise(data) -> str:
    return json.dumps(data, default=_json_default)


def _json_default(o):
    return o.__dict__


def replace_current_project(project: Project,
                            path: str = ARCHIVE_LOCATION) -> None:
    file_lines = read_file_lines(path)
    block = "\n".join(file_lines[1:])

    project = json_serialise(project)
    write_file(path, project + block)
