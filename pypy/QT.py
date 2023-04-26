from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow
import sys

class MyWIN(QMainWindow):
    def __init__(self):
        super(MyWIN , self).__init__()
        self.setGeometry(500 , 200 , 500 , 400)
        self.setWindowTitle("JOHN")
        self.initUI()


    def initUI(self):
        self.label = QtWidgets.QLabel(self)     
        self.label.setText("My label")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("CLICK me")
        self.b1.clicked.connect(self.clicked)


    def clicked(self):
        self.label.setText("YES YOUUU PRESSED ITT you dimwitt ")
        self.update()
    
    def update(self):
        self.label.adjustSize()
        

def window():
    app =  QApplication(sys.argv)
    win = MyWIN()
    win.show()
    sys.exit(app.exec_())

window()