class Todo:
    def __init__(self, date, time, text):
        self.date = date
        self.time = time
        self.text = text

    def log(self):
        print(self.date)
        print(self.text)
        print(self.time)
