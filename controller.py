from datetime import datetime
from view import View
from data import Data


class Controller:
    def __init__(self):
        self.__today = datetime.now()
        self.__data = Data()
        self.__view = View()
        self.__clean = False

        # Commands
        self.__cmd_add = "add"
        self.__cmd_show = "show"
        self.__cmd_delete = "d"
        self.__cmd_help = "h"
        self.__cmd_quit = "q"

    def start(self):
        if not self.__clean:
            self.cleanup()
        self.controller(input(f"Enter command (enter '{self.__cmd_help}' for help): "))

    def controller(self, cmd):
        match cmd:
            case self.__cmd_add:
                self.add()
            case self.__cmd_show:
                self.show()
            case self.__cmd_delete:
                self.delete()
            case self.__cmd_help:
                self.help()
            case self.__cmd_quit:
                exit(1)
            case _:
                self.add()

    def add(self):
        todo = input("Enter task: ")
        date = input("Due date (m/d/y): ")
        time = input("Due time: ")

        if not date:
            date = self.__today.strftime("%m/%d/%Y")

        if not time:
            time = self.__today.strftime("%H:%M:%S")

        self.__view.added_todo(self.__data.save(date, time, todo))
        self.start()

    def show(self):
        date = input("Due date (m/d/y): ")

        if not date:
            date = self.__today.strftime("%m/%d/%Y")

        self.__view.all_todos(date, self.__data.get(date))
        self.start()

    def cleanup(self):
        self.__data.cleanup(self.__today.strftime("%m/%d/%Y"))
        self.__clean = True

    def delete(self):
        task = input("Enter completed task: ")
        self.__data.delete(task)
        self.start()

    def help(self):
        self.__view.help()
        self.start()
