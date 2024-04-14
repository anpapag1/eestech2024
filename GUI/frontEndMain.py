from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QTextEdit
import sys


def mainWindow():
    app = QApplication(sys.argv)
    app.setApplicationName('MythosAI')

#window setup
    window = QWidget()
    window.setFixedSize(900, 700)
    window.setStyleSheet("background-image: url(mythosAiBckg)")


#button setup
    enterButton = QPushButton('Enter', window)
    enterButton.move(550, 600)
    enterButton.setStyleSheet("background: #a34d42;"
                              "color: white;"
                              "width: 100px;"
                              "height: 30px;"
                              "border-radius: 0;")

    enterButton.geometry()



#txt input setup
    userInput = QTextEdit(window)
    userInput.setFixedSize(300, 30)
    userInput.move(250, 600)
    userInput.setStyleSheet("background: #FFFFFF;")

#txt output setup
    appOutput = QTextEdit(window)
    appOutput.setFixedSize(500, 500)
    appOutput.move(200, 40)
    appOutput.setReadOnly(True)
    appOutput.setStyleSheet("background: transparent;"
                            "border: none;")


    window.show()
    app.exec()


mainWindow()