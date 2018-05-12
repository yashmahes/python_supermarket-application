
    
from product import Product
from checkoutregister import CheckoutRegister



#I have hard-coded a small
#number of Product instances so that products exist which can they can be checked out
inventory = {}
availableBarcodes = []

p1 = Product("123", "Milk, 2 Litres", 2, 2)

inventory["123"] = p1
availableBarcodes.append(p1.barcode)

p2 = Product("456", "Bread", 3.5, .5)



inventory["456"] = p2
availableBarcodes.append(p2.barcode)

p3 = Product("1523", "Beer", 5.9, 2)

inventory["1523"] = p3
availableBarcodes.append(p3.barcode)



p4 = Product("11221", "chicken", 7.5, 1.5)

inventory["11221"] = p4
availableBarcodes.append(p4.barcode)



def addProducts(checkout_Register):    
    print("----- Welcome to FedUni checkout! -----")
    
    
    while True:
        barcode = input("Please enter the barcode of your item: ")
        
        if barcode in availableBarcodes:
            
        
            my_product = inventory[barcode]
            
            print(my_product.get_name_plus_price())
            checkout_Register.scan_item(my_product)
            
        else:
            print("This product does not exist in our inventory.")
            
        
        
        scan_again = input("Would you like to scan another product? (Y/N): ")
        scan_again = scan_again.lower()
        
        if scan_again == "n":
            break
        
        
        
    
    
    

# Function to: get the money from the user 
def get_float(prompt):

    # _initializing the money to 0.0
    value = float(0.0)

    # keep asking the user until he enters the valid money
    while True:
        try:
            # take input from the user and convert it to float
            value = float(input(prompt))

    # if user enters negative money then display a message and ask again
            if value < 0.0:
                print("We don't accept negative money!")
                continue

            # if user enters valid money then break loop
            break

        # if user enters invalid money then display a message
        except ValueError:
            print('Please enter a valid floating point value.')

    # return the money entered by user
    return value
    


def makePayment(checkout_Register):
    while checkout_Register.total_cost > checkout_Register.amount_received:
        prompt = ("Payment due: $" + str(checkout_Register.total_cost - checkout_Register.amount_received) + " . Please enter an amount to pay: ")
        money = get_float(prompt)
        checkout_Register.accept_payment(money)
        


# Function to: add products in bag
def bag_products(product_list):
    
# initialize bag and non_bagged_items to empty and MAX_BAG_WEIGHT to 5.0
    bag_list = []
    non_bagged_items = []
    MAX_BAG_WEIGHT = 5.0

    # to iterate over product_list to get  product
    for product in product_list:



        # weight of product is more than 5.0 then remove this product
 # from product_list and add the product to non_bagged_items
        if product.weight > MAX_BAG_WEIGHT:
            product_list.remove(product)
            non_bagged_items.append(product)

    # initialize the current bag contents to empty and current bag wt =0
    current_bag_contents = []
    current_bag_weight = 0.0

    # loop until there is no product in the product list
    while len(product_list) > 0:

        # remove the product from the product_list located at index 0 #and store in temp_product
        temp_product = product_list[0]
        product_list.remove(temp_product)

     # if sum of weight of current bag and temp_product is less than 5.0 
        if current_bag_weight + temp_product.weight < MAX_BAG_WEIGHT:            

            # then add this product to current bag
            current_bag_contents.append(temp_product)
            current_bag_weight += temp_product.weight
            
            # if product list is empty then add current_bag_contents to bag list
            if (len(product_list) == 0):
                bag_list.append(current_bag_contents)
                
  # if sum of weight of current bag and temp_product is not less than
 #  5.0 then add current_bag_contents to bag list

        else:
            bag_list.append(current_bag_contents)

            # initialize the current bag contents to empty and current #bag wt = 0.0
            current_bag_contents = []
            current_bag_weight = 0.0

    # outputs the bag and index contents of the bag_list
    for index, bag in enumerate(bag_list):
        output = 'Bag ' + str(index + 1) + ' contains: '

        # iterate over each product in bag
        for product in bag:
            output += product.name + '\t'
        print(output, '\n')

    # if there is any non bagged item then output them
    if (len(non_bagged_items) > 0):
        output = 'Non-bagged items: '

        # iterate over each item in non bagged items
        for item in non_bagged_items:
            output += item + '\t'
        print(output,'\n')

 

while True:
    
    
    checkout_Register = CheckoutRegister()
    addProducts(checkout_Register)
    makePayment(checkout_Register)
    checkout_Register.print_receipt()
    
    print("Thank you for shopping at FedUni!")
        
        
    nextCust = input("(N)ext customer, or (Q)uit?  ")
    
        
    if nextCust == "Q":
            print("Byeeeeee")
            break
