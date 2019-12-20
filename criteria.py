class Criteria:
    __annualIR = ""
    __loanToIncome = ""

    def annualInterestPayment(self, dataClient):
        self.__annualIR = float(dataClient["Requested loan amount"]) * float(dataClient["Interest rate"])
        # print(self.__annualIR)
        pass
    
    def loanToIncome(self, dataClient):
        self.__loanToIncome = float(dataClient["Requested loan amount"]) / float(dataClient["Income"])
        # print(self.__loanToIncome)
        pass

    def isValidLoan(self, dataClient):
        print(self.__annualIR)
        print((20 / 100) * float(dataClient["Income"]))
        if (self.__annualIR > (20 / 100) * float(dataClient["Income"])):
            print("1")
            return False
        elif (self.__loanToIncome > 4):
            print("2")
            return False
        elif (float(dataClient["Credit Score"]) < 600):
            print("3")
            return False
        else:
            return True
