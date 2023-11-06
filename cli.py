from datetime import datetime
from todo import Todo


class CLI:
    def __init__(self):
        self.today = datetime.now()

    def start(self):
        self.controller(input("Press 'add' for add, 'q' for quit: "))

    def controller(self, cmd):
        match cmd:
            case "add":
                self.add()
            case "q":
                exit(1)
            case _:
                self.add()

    def add(self):
        todo = input("Enter to do: ")
        date = input("Due date (enter for today): ")
        time = input("Due time: ")

        if not date:
            date = self.today.strftime("%m/%d/%Y")

        if not time:
            time = self.today.strftime("%H:%M:%S")

        self.save(Todo(date, time, todo))
        self.start()

    def save(self, todo):
        with open("todo.txt", "a") as f:
            f.write(f"{todo.log()}\n")
