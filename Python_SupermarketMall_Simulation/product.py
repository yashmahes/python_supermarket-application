




class Product:
    def __init__(self, barcode, name, price, weight):
        self.barcode = barcode
        self.name = name
        self.price = price
        self.weight = weight
        
        
    def get_name_plus_price(self):
        return self.name + " - $" + str(self.price)
    
    
