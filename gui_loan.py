from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QDialogButtonBox, QVBoxLayout, QGroupBox, QFormLayout, QLabel, QLineEdit, QComboBox, QSpinBox, QDialog
import sys


class GUI_Loan(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self, fields):
        super(GUI_Loan, self).__init__()
        print(fields)
        self.createFormGroupBox(fields)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Form Loan")



    def createFormGroupBox(self, fields):
        self.formGroupBox = QGroupBox("Enter client information")
        layout = QFormLayout()
        for key in fields:
            if (key == "First name" or key == "Last name"):
                layout.addRow(QLabel(key + ":"), QLineEdit())
            else:
                layout.addRow(QLabel(key + ":"), QSpinBox())
        self.formGroupBox.setLayout(layout)
        pass

# App = QApplication(sys.argv)
# gui = GUI_Loan()
# gui.show()
# sys.exit(App.exec())