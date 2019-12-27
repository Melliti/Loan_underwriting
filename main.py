import criteria
import gui_loan
from PyQt5.QtWidgets import QApplication
import sys

class Main:
    client =  {
        "First name": "",
        "Last name": "",
        "Social security number": "",
        "Requested loan amount": "",
        "Loan duration": "",
        "Interest rate": "",
        "Income": "",
        "Credit score": "",
    }

    testClient =  {
        "first name": "Mazir",
        "Last name": "Melliti",
        "Social security number": "121102934",
        "Requested loan amount": "20000",
        "Loan duration": "24",
        "Interest rate": "5",
        "Income": "40000",
        "Credit Score": "898",
    }

    def isValidName(self):
        firstname = self.client["Social security number"].replace('-', '')
        lastname = self.client["Last name"].replace('-', '')
        if (len(lastname) < 2 or len(firstname) < 2):
            raise Exception("[Input Error] firstname and lastname must have at least 2 character")
        

    def isValidSocialSecurity(self):
        ssn = self.client["Social security number"].replace('-', '')
        if (len(ssn) != 9):
            raise Exception("[Input Error] Social Security number must have 9 digits")
        if not (ssn.isnumeric()):
            raise Exception("[Input Error] Social Security number must have 9 digits")        

    def isValidValues(self):
        for c in list(self.client)[3: len(self.client)]:
            if not (self.client[c].isnumeric()):
                raise Exception("[Input Error] " + c + " must contains only digits")

    def isValidCreditScore(self):
        cs = int(self.client["Credit score"])
        if (cs < 300 or cs > 850):
            raise Exception("[Input Error] Credit score is between 300 and 850")


    def main(self):
        for val in self.client.keys():
            self.client[val] = input(val + ": ")

        try:
            self.isValidName()
            self.isValidSocialSecurity()
            self.isValidValues()
            self.isValidCreditScore()
        except Exception as error:
            print(error)
            exit()

st = Main()

App = QApplication(sys.argv)
gui = gui_loan.GUI_Loan(st.client)
gui.show()

sys.exit(App.exec())
