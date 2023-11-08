class Todo:
    def __init__(self, date, time, text):
        self.__date = date
        self.__time = time
        self.__text = text

    def log(self):
        return f"{self.__date}*{self.__time}*{self.__text}"
