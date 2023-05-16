class Bank:
    def __init__(self):
        self.customers = frozenset()  # create an empty set of customers
    
    def add_customer(self, customer):
        self.customers = self.customers.union({customer})  # add the customer to the set of customers
    
    def remove_customer(self, customer):
        self.customers = self.customers.difference({customer})  # remove the customer from the set of customers

    def get_customers(self):
        return self.customers  # return the set of customers
		
bank = Bank()

# add some customers to the bank
bank.add_customer("Alice")
bank.add_customer("Bob")
bank.add_customer("Charlie")

# print the list of customers
print(bank.get_customers())

# remove a customer from the bank
bank.remove_customer("Bob")

# print the updated list of customers
print(bank.get_customers())

frozenset({'Bob', 'Charlie', 'Alice'})
frozenset({'Charlie', 'Alice'})