class atm(object):
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    
    def CashWithDrawl(self):
        print('Cash withdrawn')
    
    def BalanceEnquiry(self):
        print("Balanced enquired")
    
    def CashDebited(self):
        print("Cash Debited")

Cash=atm('237YZ9',7379139)
print(Cash.cardNumber)
print(Cash.CashWithDrawl())