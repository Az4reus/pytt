class Task(object):
    def __init__(self, title, pid, is_done=False, is_hidden=False):
        self.title = title
        self.is_done = is_done
        self.is_hidden = is_hidden
        self.pid = pid

    def do(self):
        self.is_done = True
        return self

    def hide(self):
        self.is_hidden = True
        return self

    def stringify(self) -> str:
        if self.is_hidden:
            return

        return "{:>03} | {:<68} | {} |"\
            .format(self.pid, self.title, "o" if self.is_done else " ")

    def stringify_info(self):
        return "#{:03} | {} \n {} \n".format(
            self.pid,
            "o" if self.is_done else " ",
            self.title
        )