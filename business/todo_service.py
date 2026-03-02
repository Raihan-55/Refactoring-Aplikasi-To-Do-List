class TodoService:
    def __init__(self, repository):
        self.repository = repository

    def add_task(self, task):
        if not task.strip():
            raise ValueError("Task tidak boleh kosong")

        self.repository.add(task)

    def get_all_tasks(self):
        return self.repository.get_all()