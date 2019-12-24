from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QDialogButtonBox, QVBoxLayout, QGroupBox, QFormLayout, QLabel, QLineEdit, QComboBox, QSpinBox, QDialog, QMessageBox
import sys
import criteria


class GUI_Loan(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self, fields):
        super(GUI_Loan, self).__init__()
        self.fields = fields
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
        cr = criteria.Criteria()
        cr.annualInterestPayment(self.fields)
        cr.loanToIncome(self.fields)
        if (cr.isValidLoan(self.fields)):
            QMessageBox.information(self, "Accepted", self.fields["Last name"].displayText() + " can get the loan")
        else:
            QMessageBox.critical(self, "Refused", self.fields["Last name"].displayText() + " can not get the loan")
            


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