import re

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.discount = discount
        self.items = []
        self.last_transaction = 0.0

    def add_item(self, item_name, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item_name] * quantity)
        self.last_transaction = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.total * self.discount) / 100
            self.total -= discount_amount
            self.total = round(self.total, 2)
            print(f"After the discount, the total comes to ${int(self.total) if self.total.is_integer() else self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0.0

    def reset_register_totals(self):
        self.total = 0.0
        self.items = []
        self.last_transaction = 0.0