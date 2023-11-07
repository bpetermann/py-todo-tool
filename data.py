from todo import Todo


class Data:
    def __init__(self):
        self.file = "todo.txt"

    def get(self, date):
        output = []
        with open(self.file) as f:
            for line in f:
                parts = line.strip().split("*")
                if len(parts) >= 3 and date == parts[0]:
                    output.append((parts[1], parts[2]))
        output.sort(key=lambda tup: tup[0])
        print(output)

    def save(self, date, time, todo):
        todo = Todo(date, time, todo)
        with open(self.file, "a") as f:
            f.write(f"{todo.log()}\n")
