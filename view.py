from termcolor import cprint


class View:
    def all_todos(self, date, todos):
        cprint(date, "blue")
        for todo in todos:
            print(*todo)
        cprint("----------", "blue")

    def added_todo(self, todo):
        cprint("added:", "magenta")
        print("\n".join(todo.log().split("*")))
        cprint("----------", "magenta")

    def deleted_todo(self, todo):
        cprint("completed:", "green")
        print("\n".join(todo.log().split("*")))
        cprint("----------", "green")

    def help(self):
        help_text = """
        Commands:

          'add'      Add a new task
          'show'     Show the list of tasks
          'd'        Delete a task
          'q'        Quit the program
        """
        print(help_text)
