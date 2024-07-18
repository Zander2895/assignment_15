class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget
    
    def get_category_name(self):
        return self.__category_name
    
    def set_category_name(self, category_name):
        self.__category_name = category_name
    
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_allocated_budget(self, allocated_budget):
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget
            self.__remaining_budget = allocated_budget
        else:
            raise ValueError("Allocated budget must be a positive number.")
    
    def get_remaining_budget(self):
        return self.__remaining_budget
    
    def add_expense(self, amount):
        if amount > 0:
            if amount <= self.__remaining_budget:
                self.__remaining_budget -= amount
            else:
                raise ValueError("Expense amount exceeds remaining budget.")
        else:
            raise ValueError("Expense amount must be positive.")
    
    def display_category_summary(self):
        print(f"Category: {self.get_category_name()}")
        print(f"Allocated Budget: {self.get_allocated_budget()}")
        print(f"Remaining Budget: {self.get_remaining_budget()}")

def main():
    category_name = input("Enter the category name: ")
    allocated_budget = float(input("Enter the allocated budget: "))
    
    category = BudgetCategory(category_name, allocated_budget)
    
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Budget Summary")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            try:
                expense = float(input("Enter the expense amount: "))
                category.add_expense(expense)
                print("Expense added successfully.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            category.display_category_summary()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
