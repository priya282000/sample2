import ast
import pickle
my_dict = {"Name": [], "Address": [], "Phone": [], "Balance": []}


class Bankaccount:
    def __init__(self):
        self.balance=0

    def deposit(self):
        depo=int(input("Enter the amount to deposit: "))
        self.balance+=depo
        print("Your balance is: %d"%self.balance)

    def withdraw(self):
        withd=int(input("Enter the amount to withdraw: "))
        if(withd<self.balance):
            self.balance-=withd
            print("Your balance is: %d"%self.balance)
        else:
            print("Insufficient funds")

    def display_balance(self):
        print("Your balance amount is: %d"%self.balance)
        my_dict["Balance"].append(self.balance)


class Customer(Bankaccount):
    def __init__(self):
        self.name=None
        self.address=None
        self.phone=None
        super().__init__()

    def get_name(self):
        name=input("Enter your name: ")
        self.name=name
        if len(self.name)>0:
            my_dict["Name"].append(self.name)
        else:
            print("Invalid name")

    def get_address(self):
        address=input("Enter your address: ")
        self.address=address
        if len(self.address)>0:
            my_dict["Address"].append(self.address)
        else:
            print("Invalid address")

    def get_phone(self):
        phone=int(input("Enter your phone number: "))
        self.phone=phone
        if len(str(phone))==10:
            my_dict["Phone"].append(self.phone)
        else:
            print("Invalid phone number")
        return self.phone

    def get_details(self):
        # print("Name: "+self.name+"Address: "+self.address+"Phone: "+self.phone+"Balance: "+self.balance)
        print(my_dict)
        try:
            write_file = open('data_file.obj', 'ab')
            write_file.write("\n")
            write_file.write(str(my_dict))
            write_file.close()

        except:
            print("Error in storing data")


if __name__ == '__main__':
        obj=Customer()
        obj.get_name()
        obj.get_address()
        obj.get_phone()
        obj.deposit()
        obj.withdraw()
        obj.display_balance()
        obj.get_details()