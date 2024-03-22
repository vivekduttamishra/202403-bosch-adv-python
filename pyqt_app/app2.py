
from  PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
import sys




def main():
    #step 1: create the application. without application PyQt will no work
    app = QApplication(sys.argv)

    #step 2: create the main window
    win = QMainWindow()
    win.setWindowTitle('Author Manager')
    win.resize(1024,768)

    height=40
    width=200
    ax=100
    ay=200

    #step 3: Add controls (UI) to the main window
    nameLabel=QLabel("Name",win)
    nameLabel.setGeometry(ax,ay, width, height)

    nameEdit=QLineEdit(win)
    nameEdit.setGeometry(ax+width, ay, width, height)

    saveButton=QPushButton("Save", win)
    saveButton.setGeometry(ax,ay+height, width*2, height)   

    saveButton.clicked.connect(save) 


    #step 3: show the main window
    win.show()

    #step 4: start the application
    exit_code= app.exec_()
    sys.exit(exit_code)



def save():
    print("Saving the record...")


if __name__=='__main__':
    main()