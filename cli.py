from datetime import datetime
from data import Data


class CLI:
    def __init__(self):
        self.today = datetime.now()
        self.data = Data()
        self.clean = False

    def start(self):
        if not self.clean:
            self.cleanup()
        self.controller(input("Enter 'add' for add, 'show' for show, 'q' for quit: "))

    def controller(self, cmd):
        match cmd:
            case "add":
                self.add()
            case "show":
                self.show()
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

        self.data.save(date, time, todo)
        self.start()

    def show(self):
        date = input("Due date (enter for today): ")

        if not date:
            date = self.today.strftime("%m/%d/%Y")

        self.data.get(date)

    def cleanup(self):
        self.data.cleanup(self.today.strftime("%m/%d/%Y"))
        self.clean = True
