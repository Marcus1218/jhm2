#price input
price_input = float(input("Enter the price: "))
#another price input
another_price = float(input("Enter the another price: "))
#Confilm this is my code so i use define function
def MARCUS():
    #if condition to check are larger then the price
    if price_input > another_price:
        print("The prices are larger than the second one")
    #else if condition to check smaller than price
    elif price_input < another_price:
        print("The prices are smaller than the second one")
    #else if condition to check the prices are same
    elif price_input == another_price:
        print("The prices are same")
# run my define
MARCUS()