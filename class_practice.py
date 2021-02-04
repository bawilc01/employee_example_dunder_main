'''Class Example'''


class Employee:
    num_of_emps = 0
    raise_amount = 1.06
    bonus_amount = 0.03

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    # using self.raise_amount will allow changes to specific instances
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def calc_bonus(self):
        bonus = self.pay * self.bonus_amount
        return int(bonus)

    # uses class variable to set amount across all employees
    # same as Employee.set_raise_amt(1.05)
    # can set different employees raise amount per class instance to override
    # good for one offs

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # using class method as alternative constructor
    # sets first, last, pay = what is connected by the hypen
    # splits off hypen from string values, example could be that they come in this way on csv
    # changes pay to an int for arithmetic functions
    # returns them back as values for each first last and pay variables set in the init function
    # new dev_1 can now use this method on Employee and the argument is the string value in emp_str_2

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        pay = int(pay)
        return cls(first, last, pay)

    # does not take in self or cls
    # not dependent on anything in the class or instance
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    # change bonus amount of employees in the subclass only
    bonus_amount = 0.1

    def __init__(self, first, last, pay, prog_lang):
        # parent class Employee will pass its first, last, and pay values using super and init
        # keeps code DRY
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    @classmethod
    def from_string(cls, dev_str):
        first, last, pay, prog_lang = dev_str.split('-')
        pay = int(pay)
        return cls(first, last, pay, prog_lang)


class Manager(Employee):
    def __init__(self, first, last, pay, dept, employees=None):
        # parent class Employee will pass its first, last, and pay values using super and init
        # keeps code DRY
        super().__init__(first, last, pay)
        self.dept = dept
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    @classmethod
    def from_string(cls, dev_str):
        first, last, pay, dept = dev_str.split('-')
        pay = int(pay)
        return cls(first, last, pay, dept)

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            return f'{emp.fullname()}'


dev_str_1 = 'Maisy-Miller-78000-Python'
dev_1 = Developer.from_string(dev_str_1)

dev_str_2 = 'Joe-Brown-100000-Python'
dev_2 = Developer.from_string(dev_str_2)

mgr_str_1 = 'Sam-Smith-120000-Eng'
mgr_1 = Manager.from_string(mgr_str_1)

mgr_1.add_emp(dev_1)
mgr_1.add_emp(dev_2)

emp_list = mgr_1.print_emp()

import datetime

my_date = datetime.date(2021, 1, 31)


def main(logger):
    # logger.info(f'Employee 1 Full Name: {emp_1.fullname()}')
    # logger.info(f'Employee 1 Email: {emp_1.email}')
    # logger.info(f'Employee 1 Original Pay: {emp_1.pay}')
    # logger.info(f'Raise amount: {emp_1.raise_amount}')
    # emp_1.apply_raise()
    # logger.info(f'Employee 1 Pay with Raise: {emp_1.pay}')
    # # logger.info(f'Employee name space: {emp_1.__dict__}')
    # # logger.info(f'Class name space: {Employee.__dict__}')
    # logger.info(f'Number of Employees (created): {Employee.num_of_emps}')

    logger.info(f'Employee 2 Full Name: {dev_1.fullname()}')
    logger.info(f'Employee 2 Email: {dev_1.email}')
    logger.info(f'Employee Programming Language: {dev_1.prog_lang}')
    logger.info(f'Employee 2 Original Pay: {dev_1.pay}')
    logger.info(f'Raise amount: {dev_1.raise_amount}')
    dev_1.apply_raise()
    logger.info(f'Employee 2 Pay with Raise: {dev_1.pay}')
    logger.info(f'Bonus percentage: {dev_1.bonus_amount}')
    bonus = dev_1.calc_bonus()
    logger.info(f'Employee 2 Bonus Amount: {bonus}')
    # logger.info(f'Employee name space: {dev_1.__dict__}')
    # logger.info(f'Class name space: {Employee.__dict__}')
    logger.info(f'Number of Employees (created): {Employee.num_of_emps}')
    logger.info(f'Is workday: {Employee.is_work_day(my_date)}')
    logger.info(f'Manager: {mgr_1.fullname()}')
    logger.info(f'Employees: {emp_list}')
