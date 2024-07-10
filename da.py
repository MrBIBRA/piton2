from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton

app = QApplication([])
main_win = QApplication()





main_win.show()
app.exec_()



mw.setWindowTitle('Конкурс від Crazy People')

question = QLabel('В якому році канал отримав «золоту кнопку» від YouTube?')

btn1 = QRadioButton('2005')
btn2 = QRadioButton('2010')
btn3 = QRadioButton('2015')
btn4 = QRadioButton('2020')

main_line = QVBoxLayout()

lineH1 = QHBoxLayout()
lineH2 = QHBoxLayout()
lineH3 = QHBoxLayout()

lineH1.addWidget(question, alignment = Qt.AlignCenter)
lineH2.addWidget(btn1, alignment = Qt.AlignCenter)
lineH2.addWidget(btn2, alignment = Qt.AlignCenter)
lineH3.addWidget(btn3, alignment = Qt.AlignCenter)
lineH3.addWidget(btn4, alignment = Qt.AlignCenter)

main_line.addLayout(lineH1)
main_line.addLayout(lineH2)
main_line.addLayout(lineH3)

mw.setLayout(main_line)