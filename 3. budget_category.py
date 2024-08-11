from budget_category import BudgetCategory

# Create instances of BudgetCategory
food_category = BudgetCategory("Food", 500)
entertainment_category = BudgetCategory("Entertainment", 300)

# Add expenses
food_category.add_expense(100)
entertainment_category.add_expense(50)

# Display category summaries
food_category.display_category_summary()
entertainment_category.display_category_summary()
