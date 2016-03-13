import json
from typing import List
from src.utils import write_file, read_file_lines
from src.classes.project import Project

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


def make_current_project(project_id: int) -> Project:
    from src.reconstruct import load_archive

    all_projects = load_archive()

    sought_project = None
    for p in all_projects:
        if p.pid == project_id:
            sought_project = p

    all_projects.remove(sought_project)
    new_projects = [sought_project] + all_projects
    replace_archive(new_projects)
    return sought_project


def replace_current_project(project: Project,
                            path: str = ARCHIVE_LOCATION) -> None:
    file_lines = read_file_lines(path)
    block = "\n".join(file_lines[1:])

    project = json_serialise(project)
    write_file(path, project + '\n' + block)
