class Todo:
    def __init__(self, date, time, text):
        self.date = date
        self.time = time
        self.text = text

    def log(self):
        return f"{self.date}*{self.time}*{self.text}"
