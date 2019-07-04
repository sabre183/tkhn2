from src.menuControl import menu_control


def worker_menu():
    print("hello world")
    input_dict = {'1': 'Database.new_worker()', 'q': 'exit(0)'}
    return menu_control(input_dict)
