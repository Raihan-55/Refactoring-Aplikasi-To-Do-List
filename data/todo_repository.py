class TodoRepository:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def get_all(self):
        return self.tasks