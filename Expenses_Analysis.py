
import pandas as pd
import os
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"

# Create CSV with header if it doesn't exist
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILE_NAME, index=False)

# Add expense
def add_expense():
    date = input("Enter date (yyyy-mm-dd): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")

    try:
        amount = float(amount)
    except:
        print("Amount must be a number!")
        return

    new_row = pd.DataFrame([[date, category, amount]], columns=["Date", "Category", "Amount"])
    new_row.to_csv(FILE_NAME, mode='a', header=False, index=False)
    print("Expense added successfully!\n")

# View expenses
def view_expenses():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses found.\n")
        return
    print("\nAll Expenses:\n")
    print(df)

# Summary by category with chart
def summary_by_category():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses to summarize.\n")
        return

    summary = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    print("\nTotal Expenses by Category:\n")
    print(summary)

    # Plot bar chart
    summary.plot(kind="bar", color="skyblue", figsize=(8,5))
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.show()

# Main menu
def main():
    while True:
        print("\n1. Add Expense \n2. View Expenses  \n3. Summary   \n4. Exit" )

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary_by_category()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()







