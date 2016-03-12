from src.classes.task import Task
from typing import List


class Project(object):
    def __init__(self, title: str, pid: int, tasks: List[Task] = None):
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
        if self.tasks == []:  # Why is an empty list falsy? Python, please.
            return True

        status = [t.is_done for t in self.tasks]
        return False not in status

    def do_task(self, pid: int):
        for t in self.tasks:
            if t.pid == pid:
                t.do()

        return self

    def del_task(self, pid) -> Task:
        for t in self.tasks:
            if t.pid == pid:
                self.tasks.remove(t)
                return t

        raise IndexError

    def clear(self):
        for t in self.tasks:
            if t.is_done:
                self.del_task(t.pid)

        self.reassign_pids()

    def reassign_pids(self):
        for index, t in enumerate(self.tasks):
            t.pid = index + 1

    def stringify(self) -> str:
        header = "{:03} | {:<70}\n".format(self.pid, self.title)
        separator = '=' * 80 + '\n'
        body = "\n".join([t.stringify() for t in self.tasks])

        return header + separator + body

    def one_line_stringify(self) -> str:
        return "{:03} | {:<56} | {:02}/{:02} remaining".format(
            self.pid,
            self.title,
            self._tasks_remaining(),
            self._tasks_total()
        )

    # Helper functions past here.

    def _next_pid(self) -> int:
        return len(self.tasks) + 1

    def _tasks_total(self) -> int:
        return len(self.tasks)

    def _tasks_remaining(self) -> int:
        remaining = 0
        for t in self.tasks:
            if not t.is_done:
                remaining += 1

        return remaining
