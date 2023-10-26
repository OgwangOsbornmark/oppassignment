#from customer import Customer
class Payment:
    from customer import Customer
    total_price = 0
    balance = 0
    credit = 0
    def __init__(self,price):
        self.price = price

    def __str__(self) -> str:
        return f'shs.{self.price}'

    @classmethod
    def set_total_price(cls,prdt1,prdt2,prdt3,prdt4):

              from customer import Customer
              #cls.total_price = prdt1+prdt2+prdt3+prdt4
              if Customer == True:
                cls.total_price = 0.5*(prdt1+prdt2+prdt3+prdt4)
              else:
               cls.total_price =prdt1+prdt2+prdt3+prdt4 
    @classmethod
    def get_total_price(cls):
        return cls.total_price        

    def get_balance(self):
        if self.price < self.total_price:
            return self.total_price-self.price

        
    def get_credit(self):
        if self.price > self.total_price:
            return self.price - self.total_price
    def __str__(self):
        return f'Paid price: {self.price}\nBalance: {self.get_balance()}\nCredit: {self.get_credit()}'    
# Payment.set_total_fees(50,100,150,600)
# print(Payment.get_total_price())

# payment1 = Payment(1000)
# print(payment1.get_balance())
# print(payment1.get_credit())
# payment2 = Payment(20000)
# print(payment2.get_balance())
# print(payment2.get_credit())