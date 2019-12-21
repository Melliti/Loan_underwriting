class Criteria:
    __annualIP = ""
    __loanToIncome = ""

    def annualInterestPayment(self, dataClient):
        self.__annualIP = float(dataClient["Requested loan amount"]) * (float(dataClient["Interest rate"]) / 100)
        pass
    
    def loanToIncome(self, dataClient):
        self.__loanToIncome = float(dataClient["Requested loan amount"]) / float(dataClient["Income"])
        pass

    def isValidLoan(self, dataClient):
        if (self.__annualIP > (20 / 100) * float(dataClient["Income"])):
            return False
        elif (self.__loanToIncome > 4):
            return False
        elif (float(dataClient["Credit score"]) < 600):
            return False
        else:
            return True
