class BankAccount:
    def __init__(self, account_number, pin, balance=0.0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def transfer(self, target_account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print(f"Successfully transferred ${amount} to account {target_account.account_number}. New balance is ${self.balance}.")
        else:
            print("Invalid transfer amount or insufficient funds.")

    def check_balance(self):
        print(f"Current balance is ${self.balance}.")

    def check_interest_rate(self):
        if self.balance < 1000:
            return 0.01
        elif self.balance < 5000:
            return 0.015
        else:
            return 0.02

    def calculate_future_value(self, years):
        rate = self.check_interest_rate()
        future_value = self.balance * ((1 + rate) ** years)
        print(f"Future value of investment after {years} years is ${future_value:.2f}.")

class BankApp:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, pin):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, pin)
            print("Account created successfully.")

    def sign_in(self, account_number, pin):
        if account_number in self.accounts and self.accounts[account_number].pin == pin:
            print("Sign in successful.")
            return self.accounts[account_number]
        else:
            print("Invalid account number or pin.")
            return None

    def forgot_pin(self, account_number, new_pin):
        if account_number in self.accounts:
            self.accounts[account_number].pin = new_pin
            print("Pin updated successfully.")
        else:
            print("Account does not exist.")

def main():
    bank_app = BankApp()

    while True:
        print("\nWelcome to the Online Banking App")
        print("1. Create an account")
        print("2. Sign in")
        print("3. Forgot pin")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            pin = input("Enter a 4-digit pin: ")
            bank_app.create_account(account_number, pin)
        elif choice == '2':
            account_number = input("Enter account number: ")
            pin = input("Enter pin: ")
            account = bank_app.sign_in(account_number, pin)
            if account:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer")
                    print("4. Check balance")
                    print("5. Check interest rate")
                    print("6. Calculate future value")
                    print("7. Sign out")
                    action = input("Select an option: ")

                    if action == '1':
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif action == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif action == '3':
                        target_account_number = input("Enter target account number: ")
                        if target_account_number in bank_app.accounts:
                            amount = float(input("Enter amount to transfer: "))
                            target_account = bank_app.accounts[target_account_number]
                            account.transfer(target_account, amount)
                        else:
                            print("Target account does not exist.")
                    elif action == '4':
                        account.check_balance()
                    elif action == '5':
                        rate = account.check_interest_rate()
                        print(f"Interest rate based on current balance is {rate * 100}%.")
                    elif action == '6':
                        years = int(input("Enter the number of years: "))
                        account.calculate_future_value(years)
                    elif action == '7':
                        print("Signing out...")
                        break
                    else:
                        print("Invalid option, please try again.")
        elif choice == '3':
            account_number = input("Enter account number: ")
            new_pin = input("Enter new 4-digit pin: ")
            bank_app.forgot_pin(account_number, new_pin)
        elif choice == '4':
            print("Thank you for using the Online Banking App. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()