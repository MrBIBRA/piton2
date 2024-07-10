class Widget():
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y

    def print_info(self):
        print("Напис:", self.text)
        print("Розташування:", self.x, self.y)

class Button(Widget):
    def __init__ (self, text, x, y, is_clicked):
        super().__init__(text, x, y)
        self.is_cliced = is_clicked
    
    def clisk(self):
        self.is_cliced=True
        print("Ви зарегестровані")

button1 = Button("Брати участь", 100, 100, False)
button1.print_info()

qustion = input("Хочете зарегеструватися в танках?")
if qustion.lower() == "так":
    button1.clisc()
else:
    print("А шкода")
