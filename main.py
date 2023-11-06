from todo import Todo
from cli import CLI
import sys


def main():
    # print(" ".join(sys.argv[1:]).upper())

    cli = CLI()
    todo, date, time = cli.add()
    todo = Todo(todo, date, time)
    todo.log()


if __name__ == "__main__":
    main()
