class Main:
    client =  {
        "first name": "",
        "Last name": "",
        "Social security number": "",
        "Requested loan amount": "",
        "Loan duration": "",
        "Interest rate": "",
        "Income": "",
        "Credit Score": "",
    }
    def main(self):
        for val in self.client.keys():
            self.client[val] = input(val + ": ")
        for val in self.client.values():
            print(val)

st = Main()
st.main()