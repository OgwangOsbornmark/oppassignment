from product import Product
from customer import Customer


prdt1 = Product('Makurone',1221)
prdt2 = Product('Maleewa',3320)
prdt3 = Product('Atapa',6700)
prdt4 = Product('Mukeene',6711)

#print(f'Product1:\n{prdt1}\nProduct2:\n{prdt2}\nProduct3:\n{prdt3}\nProduct4:\n{prdt4}')



customer1 = Customer(122,'Mercy',2000,'Makuroone',121,True)
customer2 = Customer(144,'Abbey',2500,'Maleewa',125,False)

print(f'\nCustomer1: {customer1}\n\nCustomer2: {customer2}')