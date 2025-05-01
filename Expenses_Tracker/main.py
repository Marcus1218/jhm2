#Github https://github.com/Marcus1218
import pandas as pd
from datetime import datetime
import csv
import os

expenses_df = pd.DataFrame(columns=["Date", "Description", "Amount"])

# input expense (1.Add Expense)
def add_expense():
    description = input("Enter description of expense: ")
    amount = float(input("Enter amount($): "))
    date_input = input("Enter date of expense (YYYY-MM-DD): ")
    # One More Funtion Enter to be time NOW
    if date_input == '':
        date_input = datetime.now().date()
    else:
        date_input = datetime.strptime(date_input,"%Y-%m-%d")
    new_expense = pd.DataFrame([[date_input, description, amount]], columns=["Date", "Description", "Amount"])
    global expenses_df
    expenses_df = pd.concat([expenses_df, new_expense], ignore_index=True)
    print("Expense added successfully!")
    expenses_df.to_csv('expenses.csv', index=False)
    print("Expenses saved to expenses.csv")

# Check Expenses (2.Get Expenses)
def get_expenses():
    global expenses_df
    expenses_df = pd.read_csv('expenses.csv')
    if expenses_df.empty:
        print("No expenses recorded.")
    else:
        print("Expenses:")
        print(expenses_df)

# Update the expenses
def update_expenses():
    global expenses_df
    expenses_df = pd.read_csv('expenses.csv')
    description_input = input("Enter the Description:")
    description_change = input("Enter the Description you want to change:")
    amount_input = float(input("Enter the Amount you want to change:"))
    if description_change == '':
        description_change = description_input
    if amount_input == '':
        amount_input = expenses_df.loc[expenses_df['Description'] == description_input, 'Amount']
    expenses_df.loc[expenses_df['Description'] == description_input, 'Description'] = description_change
    expenses_df.loc[expenses_df['Description'] == description_input, 'Amount'] = amount_input
    expenses_df.to_csv('expenses.csv', index=False)

def delete_expenses():
    global expenses_df
    expenses_df= pd.read_csv('expenses.csv')
    description_input = input("Enter the description you want to delete:")
    if description_input in expenses_df['Description'].values:
        expenses_df = expenses_df[expenses_df['Description']!= description_input]
        expenses_df.to_csv('expenses.csv', index=False)
        print("Expense deleted Sucessfully!")
    else:
        print("Description not found in expenses")

# Main (3.Exit)
def main():
    while True:
        print("1. Add Expense")
        print("2. Get Expenses")
        print("3. Update Expenses")
        print("4. Delete Expenses")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            get_expenses()
        elif choice == "3":
            update_expenses()
        elif choice == "4":
            delete_expenses()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()