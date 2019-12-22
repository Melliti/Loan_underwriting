from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QDialogButtonBox, QVBoxLayout, QGroupBox, QFormLayout, QLabel, QLineEdit, QComboBox, QSpinBox, QDialog
import sys


class GUI_Loan(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self, fields):
        super(GUI_Loan, self).__init__()
        self.fields = fields
        print(fields)
        self.createFormGroupBox()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.printResults)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Form Loan")

    def printResults(self):
        for fields in self.fields:
            if (fields == "First name" or fields == "Last name"):
                print(self.fields[fields].displayText())
            else:
                print(self.fields[fields].value())
            


    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Enter client information")
        layout = QFormLayout()
        for key in self.fields:
            if (key == "First name" or key == "Last name"):
                self.fields[key] = QLineEdit()
                layout.addRow(QLabel(key + ":"), self.fields[key])
            else:
                self.fields[key] = QSpinBox()
                if key == "Social security number":
                    self.fields[key].setMinimum(100000000)
                    self.fields[key].setMaximum(999999999)
                if key == "Credit score":
                    self.fields[key].setMaximum(850)
                    self.fields[key].setMinimum(300)
                if key == "Requested loan amount":
                    self.fields[key].setMaximum(2000000)
                    self.fields[key].setMinimum(5000)
                if key == "Income":
                    self.fields[key].setMaximum(2000000)
                    self.fields[key].setMinimum(20000)
                if key == "Loan duration":
                    self.fields[key].setMaximum(200)
                layout.addRow(QLabel(key + ":"), self.fields[key])
        self.formGroupBox.setLayout(layout)

# App = QApplication(sys.argv)
# gui = GUI_Loan()
# gui.show()
# sys.exit(App.exec())