class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"name: {self.name}, id: {self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, id, month_salary):
        super().__init__(name, id)
        self.month_salary = month_salary

    def calculate_salary(self):
        return self.month_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_day):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_day = work_day

    def calculate_salary(self):
        return self.daily_salary * self.work_day


zhangsan = FullTimeEmployee("zhang", 123, 5000)
lisi = PartTimeEmployee("lisi", 456, 200, 10)
zhangsan.print_info()
print(zhangsan.calculate_salary())
lisi.print_info()
print(lisi.calculate_salary())
