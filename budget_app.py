class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total_balance = sum(item["amount"] for item in self.ledger)
        return total_balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            amount = f"{item['amount']:.2f}"
            items += f"{item['description'][:23]:23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    spent = []
    total_spent = 0

    for category in categories:
        category_spent = sum(item["amount"] for item in category.ledger if item["amount"] < 0)
        spent.append({"name": category.name, "spent": category_spent})
        total_spent += category_spent

    for category in spent:
        category["percent"] = int((category["spent"] / total_spent) * 100 // 10 * 10)

    chart = title
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for category in spent:
            if category["percent"] >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    -" + "---" * len(categories) + "\n"
    longest_name_length = max(len(category["name"]) for category in spent)
    for i in range(longest_name_length):
        chart += "     "
        for category in spent:
            if i < len(category["name"]):
                chart += category["name"][i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip("\n")

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(clothing)

categories = [food, clothing]
print(create_spend_chart(categories))