from classes.task import Task
from typing import List


class Project(object):
    def __init__(self, title: str, pid: int, tasks: List[Task] =None):
        if tasks is None:
            tasks = []
        self.title = title
        self.tasks = tasks
        self.pid = pid

    def add_task(self, title):
        t = Task(title, self._next_pid())
        self.tasks.append(t)
        return self

    def is_done(self) -> bool:
        status = [t.is_done for t in self.tasks]
        return False in status

    def do_task(self, pid: int):
        for t in self.tasks:
            if t.pid == pid:
                t.do()

        return self

    def stringify(self) -> str:
        header = "{:03} | {:<70}\n".format(self.pid, self.title)
        separator = '=' * 80 + '\n'
        body = "\n".join([t.stringify() for t in self.tasks])

        return header + separator + body

    def _next_pid(self) -> int:
        return len(self.tasks) + 1