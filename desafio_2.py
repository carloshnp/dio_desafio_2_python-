import re

mock_db = {
    "users": {
        "123.456.789-00": {
            "name": "Fulano",
            "birth_date": "01/01/2000",
            "address": "Rua dos Bobos, 0 - Bairro - Cidade - UF",
            "accounts": {
                "0001-1": {
                    "balance": 0,
                    "account_statement": "",
                    "withdrawal_attempts": 0
                }
            }
        }
    }
}

MAX_WITHDRAWAL = 500
WITHDRAWAL_LIMIT = 3
AGENCY_NUMBER = "0001"
user = None
account = None

operations = {
    "1": "deposit",
    "2": "withdraw",
    "3": "account_statement",
    "4": "new_account",
    "5": "new_user",
    "6": "list_users",
    "7": "exit"
}

def menu():
    menu = " =================== Python Bank =================== "
    menu_options = {
    1: "Deposit",
    2: "Withdraw",
    3: "Account statement",
    4: "New account",
    5: "New user",
    6: "List users",
    7: "Exit"
    }
    for key, value in menu_options.items():
        menu += f"\n{key}. {value}"
    return input(menu + "\n\nPlease, select one of the options above: ")
    
def deposit():
    global mock_db
    cpf = input("Enter the CPF of the user: ")
    if cpf not in mock_db["users"]:
        print("Invalid user!")
        return

    account_number = input("Enter the account number: ")
    if account_number not in mock_db["users"][cpf]["accounts"]:
        print("Invalid account number!")
        return

    amount = float(input("Inform the amount of the deposit: "))
    if amount > 0:
        mock_db["users"][cpf]["accounts"][account_number]["balance"] += amount
        mock_db["users"][cpf]["accounts"][account_number]["account_statement"] += f"Deposit: R$ {amount:.2f}\n"
    else:
        print("Operation failed! The informed amount is invalid.")

def withdraw():
    global mock_db
    cpf = input("Enter the CPF of the user: ")
    if cpf not in mock_db["users"]:
        print("Invalid user!")
        return

    account_number = input("Enter the account number: ")
    if account_number not in mock_db["users"][cpf]["accounts"]:
        print("Invalid account number!")
        return

    if mock_db["users"][cpf]["accounts"][account_number]["withdrawal_attempts"] >= WITHDRAWAL_LIMIT:
        print("Withdrawal limit exceeded!")
        return

    amount = float(input("Inform the amount of the withdrawal: "))
    if amount > 0 and amount <= mock_db["users"][cpf]["accounts"][account_number]["balance"]:
        mock_db["users"][cpf]["accounts"][account_number]["balance"] -= amount
        mock_db["users"][cpf]["accounts"][account_number]["account_statement"] += f"Withdrawal: R$ {amount:.2f}\n"
        mock_db["users"][cpf]["accounts"][account_number]["withdrawal_attempts"] += 1
    else:
        print("Operation failed! The informed amount is invalid or exceeds the current balance.")

def account_statement():
    global mock_db
    cpf = input("Enter the CPF of the user: ")
    if cpf not in mock_db["users"]:
        print("Invalid user!")
        return

    account_number = input("Enter the account number: ")
    if account_number not in mock_db["users"][cpf]["accounts"]:
        print("Invalid account number!")
        return

    print("\n================ Account Statement ================")
    account_statement = mock_db["users"][cpf]["accounts"][account_number]["account_statement"]
    balance = mock_db["users"][cpf]["accounts"][account_number]["balance"]
    print("No transitions were made." if not account_statement else account_statement)
    print(f"\nBalance: R$ {balance:.2f}")
    print("==========================================")

def new_user():
    global mock_db
    cpf = input("Enter the CPF of the new user (format: 123.456.789-00): ")
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        print("Invalid CPF format!")
        return

    name = input("Enter the name of the new user: ")
    birth_date = input("Enter the birth date of the new user (format: dd/mm/yyyy): ")
    if not re.match(r'\d{2}/\d{2}/\d{4}', birth_date):
        print("Invalid birth date format!")
        return

    address = input("Enter the address of the new user: ")

    mock_db["users"][cpf] = {
        "name": name,
        "birth_date": birth_date,
        "address": address,
        "accounts": {}
    }

def new_account():
    global mock_db
    cpf = input("Enter the CPF of the user (format: 123.456.789-00): ")
    if cpf not in mock_db["users"]:
        print("Invalid user!")
        return

    last_digit = input("Enter the last digit of the new account number: ")
    account_number = f"{AGENCY_NUMBER}-{last_digit}"

    # Check if account number is unique in the database
    for user in mock_db["users"].values():
        if account_number in user["accounts"]:
            print("This account number already exists!")
            return

    mock_db["users"][cpf]["accounts"][account_number] = {
        "balance": 0,
        "account_statement": "",
        "withdrawal_attempts": 0
    }

def list_users():
    global mock_db
    for cpf, user_info in mock_db["users"].items():
        print({
            "CPF": cpf,
            "Name": user_info["name"],
            "Accounts": list(user_info["accounts"].keys())
        })

def main():
    print("Welcome to the Python Bank!")
    print("Please, select one of the options below:")
    while True:
        operation = menu()
        if operation in operations:
            globals()[operations[operation]]()
        else:
            print("Invalid operation, please re-select the desired option.")
            
main()