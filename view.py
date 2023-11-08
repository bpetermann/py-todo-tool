from termcolor import cprint


class View:
    def all_todos(self, date, todos):
        cprint(date, "blue")
        for todo in todos:
            print(*todo)
        cprint("----------", "blue")

    def added_todo(self, todo):
        cprint("Todo added:", "green")
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
