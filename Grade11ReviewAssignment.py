class Student():
    def __init__(self):
        self.user_name = ''  # user_name gets assigned in get_input()
        self.expenses = {  # initialize all values with zero before we ask the user for actual values
            'tuition': -1.0,
            'books': -1.0,
            'housing': -1.0,
            'transportation': -1.0,
            'food': -1.0,
            'monthly subscriptions': -1.0,
            'other': -1.0
        }

    def get_input(self):
        default_string = 'Please enter your estimated cost for {} per year as a number without the $ symbol: \n'
        self.user_name = input('Hi! Welcome to this simple post-secondary expenses calculator, what is your name? \n')
        # 'expense' here is just the keys as defined in __init__ in order to reduce code redundancy and make it easier
        # to add more expenses to this program if needed, all you need to do is change the dict in __init__
        for expense in self.expenses.keys():
            # loop through each expense and make sure the the inputted value is greater or equal to zero and is a number
            while self.expenses[expense] <= 0:
                # if the user input cannot be prased as a float an error will be raised and the user will be asked to reenter the number
                try:
                    user_input = float(input(default_string.format(expense)))
                    if user_input < 0:
                        raise ValueError
                    else:
                        self.expenses[expense] = user_input
                except ValueError:
                    print(f'Sorry{self.user_name}! The value you entered for {expense} is not a valid number or is less than zero. Please try again.')

    def calculate_expenses(self):
        # iterate through the expenses and multiply them all by four since we are assuming four years of education
        # add all items to the total and print the final total
        total = 0
        for expense_value in self.expenses.values():
            total += expense_value
        print(f'{self.user_name}, will need {str(total * 4)} dollars at the start of your post-secondary education in order to graduate debt free.')


student = Student()
student.get_input()
student.calculate_expenses()
