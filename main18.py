class Person:
    def __init__(self, name, deposit, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"

class House:
    def __init__(self, ID, price, owner):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = "for sale"

    def __str__(self):
        return f"House ID: {self.ID}, Price: {self.price}, Owner: {self.owner.name}, Status: {self.status}"

    def sell_apartment(self, buyer, loan=None):
        if loan is None:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "sold"
            print(f"The apartment with ID {self.ID} sold to {buyer.name} .")
        else:
            self.owner.deposit += self.price
            self.owner = buyer
            buyer.loan += loan
            self.status = "sold on loan"
            print(f"The apartment with ID {self.ID} is sold to {buyer.name} with a loan of {loan}.")

owner = Person("Owner", deposit=100000)
buyer = Person("Buyer", deposit=80000)
house = House(ID="123ABC", price=90000, owner=owner)

print("Before sale:")
print(owner)
print(buyer)
print(house)

house.sell_apartment(buyer)

print("\nAfter sale:")
print(owner)
print(buyer)
print(house)

house.sell_apartment(buyer, loan=5000)

print("\nAfter sale with loan:")
print(owner)
print(buyer)
print(house)