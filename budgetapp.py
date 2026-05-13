class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = self.name.center(30, "*")
        output = title + "\n"
        for item in self.ledger:
            description = item["description"]
            description = description[:23]
            amount = item["amount"]
            amount = f"{amount:7.2f}"
            output += f"{description:<23}{amount}\n"
        output += f"Total: {self.get_balance()}"
        return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, "Transfer to " + category.name)
        category.deposit(amount, "Transfer from " + self.name)
        return True

def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        spent = 0 
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(spent)
    total_spent = sum(spent_amounts)
    percentages = []
    for spent in spent_amounts:
        percentage = spent / total_spent * 100
        percentage = int(percentage / 10) * 10
        percentages.append(percentage)
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:3}|"
        for percentage in percentages:
            if percentage >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"
      
      
    chart += "    " + "---" * (len(categories)) + "-\n"
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        chart += "\n"
    if i !=max_length - 1 :
        chart += "\n"
    return chart.rstrip("\n")

food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

auto = Category("Auto")
auto.deposit(1000, "deposit")
auto.withdraw(15)

print(food)
print(create_spend_chart([food, clothing, auto]))