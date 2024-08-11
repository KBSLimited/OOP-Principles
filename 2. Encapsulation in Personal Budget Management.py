class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self._category_name = category_name
        self._allocated_budget = allocated_budget
        self._remaining_budget = allocated_budget

    def get_category_name(self):
        return self._category_name

    def set_category_name(self, category_name):
        self._category_name = category_name

    def get_allocated_budget(self):
        return self._allocated_budget

    def set_allocated_budget(self, allocated_budget):
        if allocated_budget >= 0:
            self._allocated_budget = allocated_budget
            self._remaining_budget = allocated_budget
        else:
            print("Error: Allocated budget must be a positive number.")

    def add_expense(self, amount):
        if amount > 0:
            if amount <= self._remaining_budget:
                self._remaining_budget -= amount
                print(f"${amount} expense added to {self._category_name}. Remaining budget: ${self._remaining_budget}")
            else:
                print("Error: Insufficient budget.")
        else:
            print("Error: Expense amount must be a positive number.")

    def display_category_summary(self):
        print(f"Category: {self._category_name}")
        print(f"Allocated Budget: ${self._allocated_budget}")
        print(f"Remaining Budget: ${self._remaining_budget}")
