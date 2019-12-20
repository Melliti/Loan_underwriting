class Criteria:
    __annualIR = ""
    __loanToIncome = ""

    def annualInterestPayment(self, dataClient):
        self.__annualIR = float(dataClient["Requested loan amount"]) * float(dataClient["Interest rate"])
        print(self.__annualIR)
        pass
    
    def loanToIncome(self, dataClient):
        self.__loanToIncome = float(dataClient["Requested loan amount"]) / float(dataClient["Income"])
        print(self.__loanToIncome)
        pass
