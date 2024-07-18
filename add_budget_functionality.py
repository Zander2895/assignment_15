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