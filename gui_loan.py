from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QInputDialog, QLabel, QLineEdit, QWidget, QPushButton
import sys


class GUI_Loan(QWidget):
    def __init__(self):
        super().__init__()

        self.text_name = QLineEdit(self)
        self.text_name.move(5, 5)
        self.text_name.setPlaceholderText("Enter your first name")

        self.btn = QPushButton('submit', self)
        self.btn.move(5, 45)
        self.btn.clicked.connect(self.showDialog)


    def showDialog(self):
        text, result = QInputDialog.getText(self, "Input dialog", 'Enter your name')
        if result == True:
            self.text_name.setText(str(text ))

App = QApplication(sys.argv)
gui = GUI_Loan()
gui.show()
sys.exit(App.exec())