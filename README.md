# Python Bank Application

This application simulates a simple banking system. It allows users to perform basic banking operations such as deposit, withdraw, view account statement, create a new user, create a new account, and list all users.

## Database

The application uses a mock database stored in a dictionary. The database contains users, each identified by their CPF. Each user has a name, birth date, address, and a dictionary of accounts. Each account has a balance, account statement, and a count of withdrawal attempts.

## Operations

The application supports the following operations:

1. **Deposit**: This operation asks for the user's CPF and account number, and the amount to deposit. If the user and account exist and the amount is positive, it adds the amount to the account's balance and updates the account statement.

2. **Withdraw**: This operation asks for the user's CPF and account number, and the amount to withdraw. If the user and account exist, the amount is positive, and the account has not exceeded the withdrawal limit, it subtracts the amount from the account's balance, updates the account statement, and increments the withdrawal attempts.

3. **Account Statement**: This operation asks for the user's CPF and account number. If the user and account exist, it prints the account statement and current balance.

4. **New User**: This operation asks for the new user's CPF, name, birth date, and address. If the CPF and birth date are in the correct format, it adds the new user to the database.

5. **New Account**: This operation asks for the user's CPF and the last digit of the new account number. If the user exists and the account number is unique, it adds the new account to the user in the database.

6. **List Users**: This operation prints a list of all users in the database, including their CPF, name, and account numbers.

## Running the Application

To run the application, simply execute the Python script. The application will print a welcome message and a menu of operations. Enter the number of the operation you want to perform. The application will ask for any necessary input and perform the operation. The application will continue to ask for operations until you select the "Exit" operation.

## Code Structure

The code is structured into a main function that runs the application, a menu function that prints the menu and gets the user's operation selection, and a function for each operation. The operation functions use the global mock database to perform their operations. The operation functions are stored in a dictionary that maps operation numbers to function names, allowing the main function to call the selected operation function using the `globals()` function.