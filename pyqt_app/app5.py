
from  PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QFont
import PyQt5.uic as uic

import sys



class GreetMainWindow(QMainWindow):
    def __init__(self,title="Author Manager", width=1024, height=768):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(width, height)
        #self.ui = Ui_MainWindow()
        #self.ui.setupUi(self)
        #self._initUI()
        uic.loadUi('greeting.ui',self)
        self._initEventHandlers()

    def _initUI(self):
        self.titleLabel= QLabel("Author Manager", self)
        self.titleLabel.move(100,50)
        self.titleLabel.setFont(QFont("Arial", 20, QFont.Bold))
        self.titleLabel.adjustSize()

        self.nameLabel= QLabel("Name", self)
        self.nameLabel.move(100,150)
        self.nameLabel.setFont(QFont("Arial", 15))
        self.nameLabel.adjustSize()

        self.nameTextBox=QLineEdit(self)
        self.nameTextBox.move(220,150)
        self.nameTextBox.resize(350,50)

        self.greetButton = QPushButton("Greet", self)
        self.greetButton.move(220,250)
        self.greetButton.resize(350,50)

        self.messageLabel=QLabel("Hello",self)
        self.messageLabel.move(100,350)
        self.messageLabel.setFont(QFont("Arial", 20, QFont.Bold))
        self.messageLabel.adjustSize()

    def _initEventHandlers(self):
        self.greetButton.clicked.connect(self.handle_greet)

    def handle_greet(self):
        name = self.nameTextBox.text()
        if name.strip() == "":
            name="John Doe"
        self.messageLabel.setText(f"Hello, {name}")
        self.messageLabel.adjustSize()




def main():
    #step 1: create the application. without application PyQt will no work
    app = QApplication(sys.argv)

    #step 2: create custom window
    win=GreetMainWindow()
    win.show()

    
    #step 4: start the application
    exit_code= app.exec_()
    sys.exit(exit_code)



def save():
    print("Saving the record...")


if __name__=='__main__':
    main()