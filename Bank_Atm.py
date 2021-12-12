class Atm(object):
    def __init__(self, atmCardNumber, pinNumber):
        self.atmCardNumber= atmCardNumber
        self.pinNumber = pinNumber
    def cashWithdrawl(self):
        print("cash withdrawled")
    def balanceEnquiry(self):
        print("balance=72")
def main():
    cardNumber=input("insert your card number")
    pinNumber=input("insert your pin number")
    user=Atm(cardNumber, pinNumber)
    print("balanceEnquiry")
    user.balanceEnquiry()
    print("your balance is now")
    user.cashWithdrawl()

if __name__ =="__main__":
    main()
    
