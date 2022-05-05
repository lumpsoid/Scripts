# FastAppendMD
import sys

from time import gmtime, strftime  # создавать timestamps
import codecs  # чтобы сохранять данные в utf-8 (русский язык)
from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import QApplication, QLineEdit, QLabel, QVBoxLayout, QWidget #QDesktopWidget



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "MinNotes"
        self.top = 996
        self.left = 160
        self.width = 1600
        self.height = 30
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #qtRectangle = self.frameGeometry()
        #centerPoint = QDesktopWidget().availableGeometry().center()
        #qtRectangle.moveCenter(centerPoint)
        #self.move(qtRectangle.topLeft())

        # прозрачность
        self.setWindowOpacity(0.8)

        # без рамок
        flags = QtCore.Qt.WindowType(QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        # создание главного объекта программы
        # self нужен, чтобы к этому виджету можно было обращаться вне фун init
        self.widget = QLineEdit()
        self.widget.returnPressed.connect(self.return_pressed)

        # создание лейбла где отображается куда буде записываться инфа
        self.file_path = QLabel(f'куда пишем: {file_path}')


        #self.setFixedSize(QSize(1800, 20))
        
        # формирование основного фрейма
        vboxlayout = QVBoxLayout()
        vboxlayout.addWidget(self.widget)
        self.setLayout(vboxlayout)
        self.show()
        

    def return_pressed(self):
        with codecs.open(f'E:\\Obsidian\\{strftime("%Y%m%d%H%M%S", gmtime())}.md', 'a', 'utf-8') as data:
            data.write(self.widget.text())  # выдается не локальное время
        self.widget.clear()
        


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())