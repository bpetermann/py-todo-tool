from datetime import datetime
from view import View
from data import Data


class Controller:
    def __init__(self):
        self.today = datetime.now()
        self.data = Data()
        self.view = View()
        self.clean = False

    def start(self):
        if not self.clean:
            self.cleanup()
        self.controller(input("Enter command (enter 'help' for help): "))

    def controller(self, cmd):
        match cmd:
            case "add":
                self.add()
            case "show":
                self.show()
            case "d":
                self.delete()
            case "help":
                self.help()
            case "q":
                exit(1)
            case _:
                self.add()

    def add(self):
        todo = input("Enter task: ")
        date = input("Due date (m/d/y): ")
        time = input("Due time: ")

        if not date:
            date = self.today.strftime("%m/%d/%Y")

        if not time:
            time = self.today.strftime("%H:%M:%S")

        self.view.added_todo(self.data.save(date, time, todo))
        self.start()

    def show(self):
        date = input("Due date (m/d/y): ")

        if not date:
            date = self.today.strftime("%m/%d/%Y")

        self.view.all_todos(date, self.data.get(date))
        self.start()

    def cleanup(self):
        self.data.cleanup(self.today.strftime("%m/%d/%Y"))
        self.clean = True

    def delete(self):
        task = input("Enter completed task: ")
        self.data.delete(task)
        self.start()

    def help(self):
        self.view.help()
        self.start()
