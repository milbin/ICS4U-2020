import re


class Student:
    BOLD = '\033[1m'
    RESET = '\033[0m'

    def __init__(self):
        self.user_name = ''  # user_name gets assigned in get_input()
        self.expenses = {  # initialize all values with -1 before we ask the user for actual values
            'tuition': -1,
            'books': -1,
            'housing': -1,
            'transportation': -1,
            'food': -1,
            'monthly subscriptions': -1,
            'other': -1
        }

    def get_input(self):
        default_string = 'Please enter your estimated cost for %s{}%s per year: \n' % (self.BOLD, self.RESET)
        invalid_string = 'Sorry {}! The value you entered for %s{}%s is not a valid number or is less than zero or not a number. Please try again.' % (self.BOLD, self.RESET)
        self.user_name = input('Hi! Welcome to this simple post-secondary expenses calculator, what is your name? \n')
        # 'expense' here is just the keys as defined in __init__ in order to reduce code redundancy and make it easier
        # to add more expenses to this program if needed, all you need to do is change the dict in __init__
        for expense in self.expenses.keys():
            # loop through each expense and make sure the the inputted value is greater or equal to zero and is a number
            while self.expenses[expense] <= 0:
                # if the user input cannot be prased as a float an error will be raised and the user will be asked to reenter the number
                try:
                    user_input = float(re.sub(r'^\$', '', input(default_string.format(expense))))
                    if user_input < 0:
                        raise ValueError
                    else:
                        self.expenses[expense] = user_input
                except ValueError:
                    print(invalid_string.format(self.user_name, expense))

    def calculate_expenses(self):
        # calculate the sum of expenses and multiply them all by four since we are assuming four years of education
        total = sum(self.expenses.values())
        print(f'{self.user_name}, will need %s{str(total * 4).rstrip("0").rstrip(".")}%s dollars at the start of your post-secondary education in order to graduate debt free.' % (self.BOLD, self.RESET))


student = Student()
student.get_input()
student.calculate_expenses()
