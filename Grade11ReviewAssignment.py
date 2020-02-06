class Student():
    def __init__(self):
        self.user_name = ''
        self.expenses = {  # initialize all values with zero before we ask the user for actual values
            'tuition' : -1.0,
            'books' : -1.0,
            'housing' : -1.0,
            'transportation' : -1.0,
            'food' : -1.0,
            'monthly subscriptions' : -1.0,
            'other': -1.0
        }
    def get_input(self):
        default_string = 'Please enter your estimated cost for {} per year as a number without the $ symbol: '
        # 'expense' here is just the keys defined in __init__ in order to reduce code redundancy and make it easier to
        # add more expenses to this program if needed
        for expense in self.expenses.keys():
            while self.expenses[expense] < 0:
                try:
                    user_input = float(input(default_string.format(expense)))
                    if user_input < 0:
                        raise ValueError
                    else:
                        self.expenses[expense] = user_input
                except ValueError:
                    print(f'Sorry{self.user_name}! The value you entered for {expense} is not a valid number or is less than zero. Please try again.')

    def calculate_expenses(self):
        total = 0
        for expense_value in self.expenses.values():
            total += expense_value
        print(str(total))


student = Student()
student.get_input()
student.calculate_expenses()




