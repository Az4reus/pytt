from src.classes.project import *
import pytest


class TestProject():
    def test_doing(self):
        proj = Project("Test project", 1)
        proj.add_task("This is a test task")
        proj.do_task(1)

        assert proj.tasks[0].is_done

    def test_deletion(self):
        proj = Project("Test Project", 1)
        proj.add_task(" terrible title")
        proj.del_task(1)

        assert proj.tasks == []

    def test_clear(self):
        proj = Project("test project", 1)

        proj.add_task("Test done")
        proj.add_task("test undone")
        proj.add_task("another done test")

        proj.do_task(1)
        proj.do_task(3)

        proj.clear()

        assert len(proj.tasks) == 1

    def test_done_status(self):
        proj = Project("test project", 1)

        assert proj.is_done() == True

        proj.add_task("one")
        proj.do_task(1)
        assert proj.is_done() == True

        proj.add_task("two")
        assert proj.is_done() == False

    def test_reassignment(self):
        proj = Project("test project", 1)

        proj.add_task("one undone")
        proj.add_task("two done:")
        proj.add_task("three undone")

        for index, task in enumerate(proj.tasks, 1):
            assert task.pid == index

        proj.do_task(2)
        proj.clear()

        for index, task in enumerate(proj.tasks, 1):
            assert task.pid == index
