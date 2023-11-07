from termcolor import colored, cprint


class View:
    def output(self, date, todos):
        cprint(date, "green")
        for todo in todos:
            print(*todo)
