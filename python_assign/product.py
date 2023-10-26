
class Product:
    def __init__(self,product_name,product_id):
        self.product_name = product_name
        self.product_id = product_id        
    

    def set_product_name(self,product_name):
        self.product_name = product_name


    def get_product_name(self):
        return self.product_name

    def __str__(self) -> str:
        return f'\nProductId: {self.product_id}\nProductName: {self.product_name}'    


# prdt1 = Product('Matooke',2314)
# print(prdt1)