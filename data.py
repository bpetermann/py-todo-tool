from todo import Todo


class Data:
    def __init__(self):
        self.__file = "todo.txt"

    def get(self, date):
        output = []
        with open(self.__file) as f:
            for line in f:
                parts = line.strip().split("*")
                if len(parts) >= 3 and date == parts[0]:
                    output.append((parts[1], parts[2]))
        output.sort(key=lambda tup: tup[0])
        return output

    def save(self, date, time, todo):
        todo = Todo(date, time, todo)
        with open(self.__file, "a", encoding="utf-8") as f:
            f.write(f"{todo.log()}\n")
        return todo

    def compare_dates(self, date1, date2):
        date1_parts = date1.split("/")
        date2_parts = date2.split("/")
        return date1_parts >= date2_parts

    def cleanup(self, date):
        future_todos = []

        with open(self.__file, "a+") as f:
            for line in f:
                todo_date, *parts = line.strip().split("*")
                if self.compare_dates(todo_date, date):
                    future_todos.append((todo_date, *parts))

        with open(self.__file, "w") as f:
            f.truncate(0)

        for todo in future_todos:
            self.save(*todo)

    def delete(self, todo):
        future_todos = []

        with open(self.__file, "r") as f:
            for line in f:
                parts = line.strip().split("*")
                if todo != parts[2]:
                    future_todos.append((parts))

        with open(self.__file, "w") as f:
            f.truncate(0)

        for todo in future_todos:
            self.save(*todo)
