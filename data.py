class Data:
    def __init__(self):
        self.file = "todo.txt"

    def get(self, date):
        with open(self.file) as f:
            input = f.read().split("\n")
            if len(input):
                for line in input:
                    print(f"{line.split('*')[1]} - {line.split('*')[2]}")

    def save(self, todo):
        with open(self.file, "a") as f:
            f.write(f"{todo.log()}\n")
