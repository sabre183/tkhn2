from src.databaseClass import Database


def worker_menu():
    print("hello world")
    input_dict = {'1': 'Database.new_worker()', 'q': 'exit(0)'}
    return menu_control(input_dict)


def add_worker():
    with Database() as db:
        dept_ids = db.cursor("select deptno from dept;")
        dept_ids.fetchall()
        departments = db.cursor("select * from dept;")
        departments.fetchall()
        print(type(dept_ids))
        print(type(departments))
    return

