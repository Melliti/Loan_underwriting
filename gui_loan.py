from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QComboBox, QDialog, QDialogButtonBox, QFileDialog, QFormLayout, QGroupBox, QLabel, QLineEdit, QMessageBox, QMessageBox, QPushButton, QSpinBox, QVBoxLayout, QWidget
import sys
import csv
import criteria


class GUI_Loan(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self, fields):
        super(GUI_Loan, self).__init__()
        self.fields = fields
        self.createFormGroupBox()

        # Open File button
        openBtn = QPushButton("Import CSV")
        openBtn.clicked.connect(self.fileReader)

        # Submit button
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.printResults)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        # Form
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(openBtn)
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

    def printResultsCSV(self, fields, result):
        if (result):
            QMessageBox.information(self, "Accepted", fields[0].strip() + " " + fields[1].strip() + " can get the loan")
        else:
            QMessageBox.critical(self, "Refused", fields[0].strip() + " " + fields[1].strip() + " can not get the loan")
            
    def fileReader(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '.', "CSV file (*.csv)")
        cr = criteria.Criteria()

        with open(filename[0], 'r') as csvFile:
            data = csv.reader(csvFile, delimiter=",")
            fields = []
            it = 0
            for row in data:
                if (it != 0):
                    cr.annualInterestPayment(None, row[3], row[5])
                    cr.loanToIncome(None, row[3], row[6])
                    self.printResultsCSV(row, cr.isValidLoan(row[6], row[7]))
                it += 1
         

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Enter client informations")
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