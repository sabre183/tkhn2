import src.workers as workers


class ChoiceFound(Exception):
    """Custom exception made to find proper choice in supplied dict for menu_control"""
    pass


def menu_control(dict1):
    """Function which, when passed a dict of function calls and their call inputs, will execute the proper command."""
    while True:
        choice = input('>>>')
        try:
            if choice in dict1:
                raise ChoiceFound
            if choice.lower() == 'q':
                return False
            else:
                print("Invalid selection. Try again. \n")
        except ChoiceFound:
            return eval(dict1[choice])
