class Criteria:
    __annualIP = ""
    __loanToIncome = ""

    def annualInterestPayment(self, dataClient):
        self.__annualIP = float(dataClient["Requested loan amount"].value()) * (float(dataClient["Interest rate"].value()) / 100)
        pass
    
    def annualInterestPayment(self, amount, ir):
        self.__annualIP = float(amount) * (float(ir) / 100)
        pass

    def loanToIncome(self, dataClient):
        self.__loanToIncome = float(dataClient["Requested loan amount"].value()) / float(dataClient["Income"].value())
        pass

    def loanToIncome(self, amount, income):
        self.__loanToIncome = float(amount) / float(income)
        pass

    def isValidLoan(self, dataClient):
        if (self.__annualIP > (20 / 100) * float(dataClient["Income"].value())):
            return False
        elif (self.__loanToIncome > 4):
            return False
        elif (float(dataClient["Credit score"].value()) < 600):
            return False
        else:
            return True

    def isValidLoan(self, income, cs):
        if (self.__annualIP > (20 / 100) * float(income)):
            return False
        elif (self.__loanToIncome > 4):
            return False
        elif (float(cs) < 600):
            return False
        else:
            return True
