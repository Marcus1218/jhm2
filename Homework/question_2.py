#if input was no then print the message
def no():
    print("Good! Let's play games instead.")

# if input was yes then ask the choice
def yes():
    choice = input("Enter your choice(ice-cream/cookies/candies):")
    #after input , start the loop of check input was not wrong
    while True:
        #if choice was ice-cream then print the message and break the loop
        if choice == "ice-cream":
            print("Remember to wash your hands")
            break
        #if choice was cookies then print the message and break the loop
        elif choice == "cookies":
            print("Can you share with your friends")
            break
        #if choice was candies then print the message and break the loop
        elif choice == "candies":
            print("Don't eat too much")
            break
        #if input was wrong then print the message and ask the input again
        else:
            print("Invalid input, please try again")

#main function to start the program
def main():
    while True:
        #ask the input from user
        snack_input = input("Do you want some snacks?(yes/no):")
        #if input was no then run the no function and break
        if snack_input == "no":
            no()
            break
        #if input was yes then run the yes function and break
        elif snack_input == "yes":
            yes()
            break
        #if input was wrong then print the message and ask the input again
        else:
            print("Invalid input, please try again")
#run the main function
main()