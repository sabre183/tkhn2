class Worker:
    name = ''
    surname = ''
    address = ''
    job = ''
    years = 0
    base_salary = 0.0
    addons_salary = 0.0

    def __init__(self, name, surname, address, job, years, base_salary, addons_salary):
        self.name = name
        self.surname = surname
        self.address = address
        self.job = job
        self.years = years
        self.base_salary = base_salary
        self.addons_salary = addons_salary


