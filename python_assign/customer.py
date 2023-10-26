
#regular_customer = True
class Customer:
        
    def __init__(self,customer_id,customer_name,payments_made,product_ordered,product_id,regular_customer):
        from payments import Payment
        from product import Product
        Payment.set_total_price(5000,5000,25000,10000)
        # Payment.set_total_price(
        #     float(input('Enter product1 price: ')),
        #     float(input('Enter product2 price: '),
        #           float(input('Enter product3 price: '),
        #                 float(input('Enter product4 price: '))
        #                 )))
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.payments_made = Payment(payments_made)
        self.product_ordered = Product(product_ordered,product_id)
        self.regular_customer = regular_customer

    def set_customer_name(self,customer_name):
         self.customer_name = customer_name

    def get_customer_name(self):
        return self.customer_name
    # def redular_customer(cls):
    #     from payments import Payment
    #     if cls.regular_customer == True:
         

    def __str__(self) -> str:
        return f'\nCustomerId: {self.customer_id}\nCustomerName: {self.customer_name}\nCustomerPayments: {self.payments_made}\nCustomerProduct: {self.product_ordered}'  
       
    
