class Criteria:
    __annualIP = ""
    __loanToIncome = ""

    def annualInterestPayment(self, dataClient, amount = 0, ir = 0):
        if (amount != 0):
            self.__annualIP = float(amount) * (float(ir) / 100)
        else:
            self.__annualIP = float(dataClient["Requested loan amount"].value()) * (float(dataClient["Interest rate"].value()) / 100)
        pass
    
    def loanToIncome(self, dataClient, amount = 0, income = 0):
        if (amount != 0):
            self.__loanToIncome = float(amount) / float(income)
        else:
            self.__loanToIncome = float(dataClient["Requested loan amount"].value()) / float(dataClient["Income"].value())
        pass

    def isValidLoan(self, dataClient, income = 0, cs = 0):
        if (income != 0):
            if (self.__annualIP > (20 / 100) * float(income)):
                return False
            elif (self.__loanToIncome > 4):
                return False
            elif (float(cs) < 600):
                return False
            else:
                return True
        else:
            if (self.__annualIP > (20 / 100) * float(dataClient["Income"].value())):
                return False
            elif (self.__loanToIncome > 4):
                return False
            elif (float(dataClient["Credit score"].value()) < 600):
                return False
            else:
                return True