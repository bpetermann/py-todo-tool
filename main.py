from datetime import date
from todo import Todo


def main():
    today = date.today()
    todo = Todo(today.strftime("%d/%m/%Y"), "14:00", "Clean house")
    todo.log()


if __name__ == "__main__":
    main()
