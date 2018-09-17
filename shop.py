####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Nice cupcakes"
signature_flavors = ["cinamon","pistachio","cardamom","orange","grap","apple"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print("our menu:")
    for item in menu:
        print("\t- %-25s (KD %.3f)"%(item,menu[item]))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for item in original_flavors:
        print("\t-", item,)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for item in signature_flavors:
        print("\t-", item)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    order=order.lower()
    if order not in original_flavors and order not in signature_flavors and order not in menu.keys():
        print("check and see if the order is valid in our menu")
        return False
    return True

def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    user_order=str(input("What is your order?(Enter the exact spelling of the order you want. Type (exit) to end your order)\n"))
    user_order=user_order.lower()
    while True:
        
        if user_order.lower()=="exit":
            print("-"*50)
            break;
        if is_valid_order(user_order):
            order_list.append(user_order)
        user_order=str(input()).lower()
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total>=5:
        print("you can pay by cash or credit card")
    else:
        print("only cash payment")


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for item in order_list:
        if item in signature_flavors:
            total+=signature_price
        elif item in original_flavors:
            total+= original_price
        else:
            total+=menu[item]
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for item in order_list:
        print("\t-",item)
    print()
    total=get_total_price(order_list)
    print("total price of your order is (KD %.3f)"% total)
    accept_credit_card(total)
    print("\nThank you for shopping with %s. Come again!!"%(cupcake_shop_name))


