from datetime import date


class CLI:
    def __init__(self):
        self.today = date.today()

    def add(self):
        todo = input("Enter to do: ")
        date = input("Due date (enter for today): ")
        time = input("Due time: ")

        if date == "":
            date = self.today

        return todo, date, time
