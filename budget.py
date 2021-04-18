#Question:
#Create a Budget class that can instantiate objects based on different categories like food, clothing and entertainment.
#These objectssould allow for
#1. Depositing funds inside each category
#2 WIthdrawing funds from each category
#3. Computing category balances
#4. Transferring balance amount between categories

class Budget:

    #instance attribute
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    #Deposit
    def deposit(self, amount):
        self.balance = amount

        return f"Your new balance is ${self.balance} in {self.name} budget"

    #Withdrawal
    def withdraw(self, amount):
        if self.balance <= amount:
            return "Sorry, Insufficent Funds"
        else:
            self.balance = self.balance - amount

            feedback = "_____________________\n"
            feedback +="Transaction was Successful\n"
            feedback += f"Your new balance is ${self.balance} in {self.name} budget"

            return feedback

    def get_balance(self):
           feedback = f"The cash balance for {self.name} budget is ${self.balance}"
           return feedback
    
    def transfer(self, amount, category):
        if self.name == category.name:
            feedback = "ERROR!\n"
            feedback += "You cannot transfer within the same category\n"
            feedback += "You can only make deposit a category"

            return feedback
        if self.balance < amount:

            return "Sorry, Insufficient Funds"
        else:
            self.balance-=amount
            category.balance += amount

            feedback = "________________\n"
            feedback += "Transfer was successful \n"
            feedback += f"The balance of {self.name} is ${self.balance}\n"
            feedback += f"The new balance for {category.name} is ${category.balance}"

            return feedback

#instantiating the Budget class
food = Budget("Food", 2000)
clothing = Budget("Clothing", 3000)
entertainment = Budget("Entertainment", 4000)

print(food.deposit(2000))
print("__________________________")
print(clothing.deposit(3000))
print("__________________________")
print(entertainment.deposit(4000))
print("__________________________")

#print(f"{food.name} balance is {food.balance}")

print(food.withdraw(2000))
print(clothing.withdraw(1500))
print(entertainment.withdraw(2100))

print("_________________________")

print(food.get_balance())
print("__________________________")
print(clothing.get_balance())
print("__________________________")
print(entertainment.get_balance())
print("__________________________")

print (clothing.transfer(500, food))
print("_____________")
print(food.transfer(800, food))
