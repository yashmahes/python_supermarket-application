from product import Product



class CheckoutRegister:
    def __init__(self):
        self.total_cost = 0.0
        self.product_bought = []
        self.amount_received = 0.0
        
    def accept_payment(self, some_amount):
        self.amount_received += some_amount
        
    def print_receipt(self):
        for prod in self.product_bought:
            print(prod.name + "       $" + str(prod.price))
            
        print("Total amount due:     $" + str(self.total_cost))
        print("Amount received:     $" + str(self.amount_received))
        print("Change given:     $" + str(self.amount_received - self.total_cost))
        
    def scan_item(self, some_product):
        self.product_bought.append(some_product)
        self.total_cost += some_product.price
        
        
        
    
