# IMPORTING PYTHON MODULES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# To avoid table wrapping
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# IMPORTING DATABASES
bookstable = pd.read_csv("BooksTable.csv",
                   header = 0)
custtable = pd.read_csv("CustTable.csv",
                   header = 0)
transacttable = pd.read_csv("TransactionTable.csv",
                   header = 0)

# WELCOME PAGE - 1
print("=" * 90)
print()
print(" "*31,"WELCOME TO TALES AND TAILS", " "*31) 
print(" "*32,"~ Catch your next read ~"," "*32)
print()
print("=" * 90)

# DEFINING FUNCTIONS
# 6. EXIT PAGE
def exit_app():
    print("="*90)
    print()
    while True:
        exitchoice = input("Would you like to save your changes (Y/N)? ").strip().lower()
        print()
        if exitchoice == "y":
            custtable.to_csv("CustTable.csv", index=False)
            bookstable.to_csv("BooksTable.csv", index=False)
            transacttable.to_csv("TransactionTable.csv", index=False)
            break
        elif exitchoice == "n":
            break
        else:
            print("Not a valid option. Please enter Y or N.\n")   
    print("="*90)
    print()
    print(" "*33, "THANK YOU FOR VISITING", " "*33)
    print()
    print("="*90)
    
# 1. BILLING:
def bill():
    while True: 
        print("=" * 90)
        print()
        print(" " * 35, "Welcome to Billing", " " * 35)
        print()
        print("=" * 90)
        print()
        bcname = input("Enter customer name: ").strip().lower()
        custtable["Cust_name_lower"] = custtable["Cust_name"].str.lower()
        match = custtable[custtable["Cust_name_lower"].str.contains(bcname, na=False)]
        if match.empty:
            print("\nCustomer Not Found. Try again.\n")
            continue  
        if len(match) > 1:
            print("\nMultiple customers found:")
            for i, row in match.iterrows():
                print(f"{i}. {row['Cust_name']} (Customer ID: {row['Cust_id']})")
            try:
                idx = int(input("Enter the number of the correct customer: "))
                if idx not in match.index:
                    print("Invalid choice. Try again.\n")
                    continue
                bcid = match.loc[idx, "Cust_id"]
                bcname_full = match.loc[idx, "Cust_name"]
            except ValueError:
                print("Invalid input. Try again.\n")
                continue
        else:
            bcid = match["Cust_id"].values[0]
            bcname_full = match["Cust_name"].values[0]
        try:
            bbid = int(input("Enter Book ID: "))
        except ValueError:
            print("Invalid book ID. Try again.\n")
            continue
        book_row = bookstable.loc[bookstable["Book_id"] == bbid]

        if book_row.empty:
            print("Book Not Found. Try again.\n")
            continue
        bbname = book_row["Book_name"].values[0]
        bbprice = book_row["Book_price"].values[0]
        bbdisc = book_row["Book_discount"].values[0]
        btprice = bbprice * (1 - (bbdisc) / 100)
        btnewrow = [bcid, bbname, bbid, btprice]
        transacttable.loc[len(transacttable)] = btnewrow
        print()
        print("Your Total is ₹" + str(round(btprice, 2)))
        print()
        print("Purchase Details:")
        print(f"Customer: {bcname_full}")
        print(f"Book Name: {bbname}")
        print(f"Original Price: ₹{bbprice}")
        print(f"Discount Applied: {bbdisc}%")
        print()
        print("THANK YOU FOR PURCHASING!")
        print("=" * 90)
        print()
        while True:
            print("Would you like to:")
            print("1. Purchase more\n2. Exit to Home Page\n3. Exit Application")
            try:
                bchoice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice. Try again.\n")
                continue
            print("=" * 90)
            print()
            if bchoice == 1:
                break  
            elif bchoice == 2:
                home_page()
                return
            elif bchoice == 3:
                exit_app()
                return
            else:
                print("That is not a valid option. Try again.\n")

# 2. SIGN UP:
def sign_up():
    print("="*90)
    print()
    print(" "*35,"Welcome to Sign Up"," "*35)
    print()
    print("="*90)
    print()
    suname = input("Enter your name ")
    if suname not in custtable["Cust_name"].values:  
        suphonenostr = str(input("Enter phone number "))
        while len(suphonenostr) != 10 or not suphonenostr.isdigit():
            print("Phone number not valid. Please re-enter.")
            suphonenostr = str(input("Enter phone number: "))
        suphoneno = int(suphonenostr)
        sunewrecord = [custtable["Cust_id"].max() + 1, suname, suphoneno]
        custtable.loc[len(custtable)] = sunewrecord
        print()
        print("Congratultions! You have been successfully signed up!")
        print("Your Customer ID is:", custtable["Cust_id"].tail(1).values[0])
        home_page()
    else:
        print()
        print("Sorry, this customer already exists in the database. ")
        print("Please return to homepage")
        print()
        print("="*90)
        home_page()

# 3. SEARCH DATABASE
def search_db():
    print("="*90)
    print()
    print(" "*35,"Search Database"," "*35)
    print()
    print("="*90)
    print()
    print("Which database would you like to search?")
    print("1. Customer Records\n2. Books Stock\n3. Transaction History\n4. View Full Database")
    sdbchoice = int(input("Enter your choice: "))
    print()
    if sdbchoice == 1:
        print("Search by:")
        print("1. Customer ID\n2. Customer Name\n3. Customer's Phone Number")
        sdbcchoice = int(input("Enter your choice: "))
        print()
        sdbkeyword = input("Enter keyword to search for: ").lower()
        print()
        if sdbcchoice == 1:
            try:
                sdbid = int(sdbkeyword)
                print(custtable[custtable["Cust_id"] == sdbid])
            except ValueError:
                print("Invalid ID format. Must be a number.")
        elif sdbcchoice == 2:
            print(custtable[custtable["Cust_name"].str.lower().str.contains(sdbkeyword, na=False)])
        elif sdbcchoice == 3:
            print(custtable[custtable["Cust_contact"].astype(str).str.contains(sdbkeyword, na=False)])
        else:
            print("Not a valid option. Try again.")
            sdbcchoice = int(input("Enter your choice: "))
    elif sdbchoice == 2:
        print("Search by:")
        print("1. Book ID\n2. Book Name\n3. Book Price\n4. Book Discount\n5. Book Stock")
        sdbcchoice = int(input("Enter your choice: "))
        print()
        sdbkeyword = input("Enter keyword to search for: ").lower()
        print()
        if sdbcchoice == 1:
            try:
                sdbid = int(sdbkeyword)
                print(bookstable[bookstable["Book_id"] == sdbid])
            except ValueError:
                print("Invalid ID format. Must be a number.")
        elif sdbcchoice == 2:
            print(bookstable[bookstable["Book_name"].str.lower().str.contains(sdbkeyword, na=False)])
        elif sdbcchoice == 3:
            print(bookstable[bookstable["Book_price"] == float(sdbkeyword)])
        elif sdbcchoice == 4:
            print(bookstable[bookstable["Book_discount"] == float(sdbkeyword)])
        elif sdbcchoice == 5:
            print(bookstable[bookstable["Book_stock"] == int(sdbkeyword)])
        else:
            print("Not a valid option. Try again.")
            sdbcchoice = int(input("Enter your choice: "))
    elif sdbchoice == 3:
        print("Search by:")
        print("1. Customer ID\n2. Book ID\n3. Book Title\n4. Total Price")
        sdbcchoice = int(input("Enter your choice: "))
        print()
        sdbkeyword = input("Enter keyword to search for: ").lower()
        print()
        if sdbcchoice == 1:
            try:
                sdbid = int(sdbkeyword)
                print(transacttable[transacttable["Cust_id"] == sdbid])
            except ValueError:
                print("Invalid ID format. Must be a number.")
        elif sdbcchoice == 2:
            try:
                sdbbid = int(sdbkeyword)
                print(transacttable[transacttable["Book_id"] == sdbbid])
            except ValueError:
                print("Invalid Book ID format. Must be a number.")
        elif sdbcchoice == 3:
            print(transacttable[transacttable["Title"].str.lower().str.contains(sdbkeyword, na=False)])
        elif sdbcchoice == 4:
            try:
                total = float(sdbkeyword)
                print(transacttable[transacttable["Total"] == total])
            except ValueError:
                print("Invalid number format.")
        else:
            print("Not a valid option. Try again.")
            sdbcchoice = int(input("Enter your choice: "))
    elif sdbchoice == 4:
        print("Which database would you like to view?")
        print("1. Customer Records\n2. Books Stock\n3. Transaction History")
        sdbcchoice = int(input("Enter your choice: "))
        if sdbcchoice == 1:
            print(custtable)
        elif sdbcchoice == 2:
            print(bookstable)
        elif sdbcchoice == 3:
            print(transacttable)
        else:
            print("Not a valid option. Try again.")
            sdbcchoice = int(input("Enter your choice: "))
    else:
        print("Not a valid option. Try again.")
        return search_db()
    print()
    print("="*90)
    print()
    print("How would you like to proceed?")
    print("1. Search more \n2. Exit to home page\n3. Exit Application")
    sdbchoice = int(input("Enter your choice "))
    print()
    print()
    if sdbchoice == 1:
        search_db()
    elif sdbchoice == 2:
        print()
        print("="*90)
        print()
        home_page()
    elif sdbchoice == 3:
        exit_app()
    else:
        print("That is not a valid option. Try again.")
        sdbchoice = int(input("Enter your choice "))
        print()
        
#  4. UPDATE RECORDS
def update_db():
    print("="*90)
    print()
    print(" "*35, "Update Database", " "*35)
    print()
    print("="*90)
    print()
    print("Which database would you like to update?")
    print("1. Customer Records\n2. Books Stock")
    db_choice = int(input("Enter your choice: "))
    print()
    if db_choice == 1:
        print("Update by:")
        print("1. Customer Name\n2. Customer ID")
        field_choice = int(input("Enter your choice: "))
        print()
        keyword = input("Enter keyword to find the record: ").lower()
        print()
        if field_choice == 1:
            matches = custtable[custtable["Cust_name"].str.lower().str.contains(keyword, na=False)]
        elif field_choice == 2:
            try:
                cid = int(keyword)
                matches = custtable[custtable["Cust_id"] == cid]
            except ValueError:
                print("Invalid ID format.")
                return update_db()
        else:
            print("Not a valid option.")
            return update_db()
        if matches.empty:
            print("No matching record found.")
            return update_db() 
        print("Matching record(s):")
        print(matches)
        print()
        print("Columns available to update:", list(custtable.columns))
        col = input("Enter column name to update: ")
        if col not in custtable.columns:
            print("Invalid column.")
            return update_db()
        
        new_val = input(f"Enter new value for {col}: ")
        if custtable[col].dtype in [int, float]:
            new_val = eval(new_val)
        
        custtable.loc[matches.index, col] = new_val
        print("Record updated successfully!")  
    elif db_choice == 2:
        print("Update by:")
        print("1. Book Name\n2. Book ID")
        field_choice = int(input("Enter your choice: "))
        print()
        keyword = input("Enter keyword to find the record: ").lower()
        print()
        
        if field_choice == 1:
            matches = bookstable[bookstable["Book_name"].str.lower().str.contains(keyword, na=False)]
        elif field_choice == 2:
            try:
                bid = int(keyword)
                matches = bookstable[bookstable["Book_id"] == bid]
            except ValueError:
                print("Invalid Book ID format.")
                return update_db()
        else:
            print("Not a valid option.")
            return update_db()
        
        if matches.empty:
            print("No matching record found.")
            return update_db()
        
        print("Matching record(s):")
        print(matches)
        print()
        
        print("Columns available to update:", list(bookstable.columns))
        col = input("Enter column name to update: ")
        if col not in bookstable.columns:
            print("Invalid column.")
            return update_db()
        
        new_val = input(f"Enter new value for {col}: ")
        if bookstable[col].dtype in [int, float]:
            new_val = eval(new_val)
        
        bookstable.loc[matches.index, col] = new_val
        print("Record updated successfully!")
    print()
    print("="*90)
    print()
    print("What would you like to do next?")
    print("1. Update more\n2. Exit to home page\n3. Exit Application")
    next_choice = int(input("Enter your choice: "))
    print()
    if next_choice == 1:
        update_db()
    elif next_choice == 2:
        print()
        print("="*90)
        print()
        home_page()
    elif next_choice == 3:
        exit_app()
    else:
        print("Invalid choice, try again.")
        next_choice = int(input("Enter your choice: "))
        
# 5. VIEW STATISTICS
def view_stat():
    print("="*90)
    print()
    print("Which statistic would you like to view?")
    print("1. Popularity of book in global market\n2. Popularity of book in store\n3. Frequent customers")
    vschoice = int(input("Enter your choice "))
    if vschoice == 1:
        popularity = bookstable[["Book_name", "Book_SaleRate (%)"]]
        top_books = popularity.sort_values(by="Book_SaleRate (%)", ascending=False).head(10)
        plt.figure(figsize=(8, 8))
        plt.pie(
            top_books["Book_SaleRate (%)"],
            labels=top_books["Book_name"],
            autopct='%1.1f%%',
            startangle=140,
            colors=plt.cm.tab10.colors  # 10 distinct colors
        )
        plt.title("Top 10 Most Popular Books", fontsize=14)
        plt.tight_layout()
        plt.show()
    elif vschoice == 2:
        book_counts = transacttable["Title"].value_counts()
        top_books = book_counts.head(10)
        plt.figure(figsize=(8, 8))
        plt.pie(
            top_books.values,
            labels=top_books.index,
            autopct='%1.1f%%',
            startangle=140,
            colors=plt.cm.Paired.colors 
        )
        plt.title("Top 10 Most Purchased Books", fontsize=14)
        plt.tight_layout()
        plt.show()
    elif vschoice == 3:
        merged = transacttable.merge(custtable, on="Cust_id", how="left")
        customer_counts = merged["Cust_name"].value_counts()
        top_customers = customer_counts.head(10)
        plt.figure(figsize=(10, max(len(top_customers)*0.5, 4)))
        bars = plt.barh(top_customers.index, top_customers.values, color='skyblue')
        plt.xlabel('Number of Books Purchased', fontsize=12)
        plt.ylabel('Customer Name', fontsize=12)
        plt.title('Top 10 Customers by Purchase Frequency', fontsize=14)
        plt.gca().invert_yaxis() 
        for bar in bars:
            plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                     str(int(bar.get_width())), va='center')
        plt.tight_layout()
        plt.show()
    else:
        print("That is not a valid option. Try again.")
        vschoice = int(input("Enter your choice "))
    print()
    print("="*90)
    print()
    print("Graph has been displayed")
    print()
    print("="*90)
    print()
    print("What would you like to do?")
    print("1. View another graph\n2. Exit to home page\n3. Exit Application")
    vsnext_choice = int(input("Enter your choice: "))
    print()
    if vsnext_choice == 1:
        view_stat()
    elif vsnext_choice == 2:
        print()
        print("="*90)
        print()
        home_page()
    elif vsnext_choice == 3:
        exit_app()
    else:
        print("Invalid choice, try again.")
        vsnext_choice = int(input("Enter your choice: "))

# WELCOME PAGE #2
def home_page():
    print()
    print("What would you like to do today?")
    opt = ['Billing', 'Sign Up Customer', 'Search Database', 'Update Records', 'View Statistics' , 'Exit']
    for i in range(len(opt)):
        print(str(i+1) + ". " + opt[i])
    choice = int(input("Enter your choice "))
    print()
    if choice == opt.index('Billing')+1:
        bill()
    elif choice == opt.index('Sign Up Customer')+1:
        sign_up()
    elif choice == opt.index('Search Database')+1:
        search_db()
    elif choice == opt.index('Update Records')+1:
        update_db()
    elif choice == opt.index('View Statistics')+1:
        view_stat()
    elif choice == opt.index('Exit')+1:
        exit_app()
    else:
        print("Sorry, that is not a valid option. Try again.")
        home_page()
home_page()
