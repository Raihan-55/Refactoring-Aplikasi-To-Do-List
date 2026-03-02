from data.todo_repository import TodoRepository
from business.todo_service import TodoService
from presentation.cli_controller import TodoCLI

def main():
    repository = TodoRepository()
    service = TodoService(repository)
    cli = TodoCLI(service)

    cli.run()

if __name__ == "__main__":
    main()