import os
import datetime

class Account:
    def __init__(self, nr, name, money):
        self.__nr = nr
        self.__name = name
        self.__money = money

    @classmethod
    def access_account(cls, nr, name, money):
        return cls(nr, name, money)

    @staticmethod
    def update_money(self):
        with open(f"acc_{self.__nr}.his", "r") as f:
            file = f.readlines()
        file[1] = f"Money: {self.__money}\n"
        with open(f"acc_{self.__nr}.his", "w") as f:
            f.writelines(file)

    def deposit(self, value):
        #Ask for notes to deposit
        dep100 = input(f"Number of $ 100 notes to deposit: ")
        dep50  = input(f"Number of $  50 notes to deposit: ")
        dep20  = input(f"Number of $  20 notes to deposit: ")
        dep10  = input(f"Number of $  10 notes to deposit: ")
        dep5   = input(f"Number of $   5 notes to deposit: ")
        dep1   = input(f"Number of $   1 notes to deposit: ")
        if int(value) > 0 and int(dep100)*100 + int(dep50)*50 + int(dep20)*20 + int(dep10)*10 + int(dep5)*5 + int(dep1) == int(value):
            try:
                #Read notes in ATM
                notes = []
                with open("atm_notes.bnk", "r") as file:
                    for i in file:
                        notes.append(int(i[:-1]))
                #Add notes in ATM to deposited ones
                notes[0] = str(int(notes[0]) + int(dep1)) + "\n"
                notes[1] = str(int(notes[1]) + int(dep5)) + "\n"
                notes[2] = str(int(notes[2]) + int(dep10)) + "\n"
                notes[3] = str(int(notes[3]) + int(dep20)) + "\n"
                notes[4] = str(int(notes[4]) + int(dep50)) + "\n"
                notes[5] = str(int(notes[5]) + int(dep100))
                with open(f"atm_notes.bnk", "w") as f:
                    f.writelines(notes)
                #Update account
                self.__money = str(int(self.__money.strip()) + int(value))
                with open(f"acc_{self.__nr}.his", "a") as f:
                    f.write(f"\n{str(datetime.date.today())} DEPOSIT + {value} \nMoney: {self.__money}")
                self.update_money(self)
                print("\n*** Success! ***")
            except:
                print("*** Internal error. ***")
        else:
            print("\n*** Invalid value. ***")
    
    def withdraw(self, value):
        #Read notes in ATM
        notes = []
        with open("atm_notes.bnk", "r") as file:
            for i in file:
                notes.append(int(i[:-1]))
        print("Number of $   1 notes: " + str(notes[0]))
        print("Number of $   5 notes: " + str(notes[1]))
        print("Number of $  10 notes: " + str(notes[2]))
        print("Number of $  20 notes: " + str(notes[3]))
        print("Number of $  50 notes: " + str(notes[4]))
        print("Number of $ 100 notes: " + str(notes[5]))
        ATM_money = notes[5]*100 + notes[4]*50 + notes[3]*20 + notes[2]*10 + notes[1]*5  + notes[0] 
        print("Total money in ATM: $ {}".format(ATM_money))
        #Ask for notes to withdraw
        while True:
            wit100 = input(f"Number of $ 100 notes to withdraw: ")
            if int(wit100) <= int(notes[5]):
                break
        while True:
            wit50  = input(f"Number of $  50 notes to withdraw: ")
            if int(wit50) <= int(notes[4]):
                break
        while True:
            wit20  = input(f"Number of $  20 notes to withdraw: ")
            if int(wit20) <= int(notes[3]):
                break
        while True:
            wit10  = input(f"Number of $  10 notes to withdraw: ")
            if int(wit10) <= int(notes[2]):
                break
        while True:
            wit5   = input(f"Number of $   5 notes to withdraw: ")
            if int(wit5) <= int(notes[1]):
                break
        while True:
            wit1   = input(f"Number of $   1 notes to withdraw: ")
            if int(wit1) <= int(notes[1]):
                break
        if int(value) > int(self.__money.strip()):
            print("\n*** Not enough money. ***")
        elif int(value) > 0 and int(wit100)*100 + int(wit50)*50 + int(wit20)*20 + int(wit10)*10 + int(wit5)*5 + int(wit1) == int(value):
            try:
                #Subtract notes in ATM to deposited ones
                notes[0] = str(int(notes[0]) - int(wit1)) + "\n"
                notes[1] = str(int(notes[1]) - int(wit5)) + "\n"
                notes[2] = str(int(notes[2]) - int(wit10)) + "\n"
                notes[3] = str(int(notes[3]) - int(wit20)) + "\n"
                notes[4] = str(int(notes[4]) - int(wit50)) + "\n"
                notes[5] = str(int(notes[5]) - int(wit100))
                with open(f"atm_notes.bnk", "w") as f:
                    f.writelines(notes)
                #Update account
                self.__money = str(int(self.__money.strip()) - int(value))
                with open(f"acc_{self.__nr}.his", "a") as f:
                    f.write(f"\n{str(datetime.date.today())} WITHDRAW - {value} \nMoney: {self.__money}")
                self.update_money(self)
                print("\n*** Success! ***")
            except:
                print("*** Internal error. ***")
        else:
            print("\n*** Invalid value. ***")
    
    def show_money(self):
        print("Money: " + self.__money)
    
    def show_history(self):
        with open(f"acc_{self.__nr}.his", "r") as f:
            h = f.read()
        print(h)

def login():
    name = input("Enter your name: ")
    n = input("Enter account number: ")
    if os.path.isfile(f'acc_{n}.his'):
        with open(f"./acc_{n}.his", "r") as f:
            first_line = "nothing"
            for line in f:
                if first_line != "nothing":
                    break
                first_line = line
        if first_line == f"Name: {name}\n":
            m = line[7:]
            acc = Account.access_account(n, name, m)
            del n, name, m
            while True:
                option = menu_user()
                if option == "d":
                    acc.deposit(input("Value: "))
                elif option == "w":
                    acc.withdraw(input("Value: "))
                elif option == "m":
                    acc.show_money()
                elif option == "h":
                    acc.show_history()
                elif option == "q":
                    break
                else:
                    print("\n*** Invalid operation. ***")
        else:
            print("*** Wrong credentials. ***")
    else:
        print("*** Account does not exist. ***")

def new_acc():
    name = input("Enter your name: ")
    n = 1000
    available_acc = False
    while (available_acc == False):
        if n > 9999:
            print("*** Too many accounts. ***")
            break
        elif os.path.isfile(f'acc_{n}.his'):
            n += 1
        else:
            with open(f"acc_{n}.his", "w") as f:
                f.write("Name: " + name + "\nMoney: 0\nAccount created: " + str(datetime.date.today()))
            print("Your account number is: " + str(n))
            print("Account created!")
            available_acc = True

def menu():
    menu = """
    ====== MENU ======
    [l]  LogIn
    [n]  New Account
    [q]  Quit
    => """
    return input(menu)

def menu_user():
    menu = """
    === USER MENU ===
    [d]  Deposit
    [w]  Withdraw
    [m]  Money Total
    [h]  History
    [q]  Quit
    => """
    return input(menu)

def main():
    while True:
        option = menu()
        if option == "l":
            login()
        elif option == "n":
            new_acc()
        elif option == "q":
            break
        else:
            print("\n*** Invalid operation. ***")

main()