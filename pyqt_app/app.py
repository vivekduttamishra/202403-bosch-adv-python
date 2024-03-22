
from  PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def main():
    #step 1: create the application. without application PyQt will no work
    app = QApplication(sys.argv)

    #step 2: create the main window
    win = QMainWindow()
    win.setWindowTitle('Author Manager')
    win.resize(1024,768)

    #step 3: show the main window
    win.show()

    #step 4: start the application
    exit_code= app.exec_()
    sys.exit(exit_code)



if __name__=='__main__':
    main()