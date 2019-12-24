class Criteria:
    __annualIP = ""
    __loanToIncome = ""

    def annualInterestPayment(self, dataClient):
        self.__annualIP = float(dataClient["Requested loan amount"].value()) * (float(dataClient["Interest rate"].value()) / 100)
        pass
    
    def loanToIncome(self, dataClient):
        self.__loanToIncome = float(dataClient["Requested loan amount"].value()) / float(dataClient["Income"].value())
        pass

    def isValidLoan(self, dataClient):
        print("IP")
        print(self.__annualIP)
        print((20 / 100) * float(dataClient["Income"].value()))
        print("LtI")
        print(self.__loanToIncome)
        print("CS")
        print(float(dataClient["Credit score"].value()))

        if (self.__annualIP > (20 / 100) * float(dataClient["Income"].value())):
            return False
        elif (self.__loanToIncome > 4):
            return False
        elif (float(dataClient["Credit score"].value()) < 600):
            return False
        else:
            return True
