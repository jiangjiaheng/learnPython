class Cat:
    def __init__(self, cat_name, cat_age, cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color


cat_one = Cat('brant', '2', 'red')


# print(cat_one.name, cat_one.age, cat_one.color)

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = {"lang": 0, "math": 0, "eng": 0}

    def set_grade(self, course, point):
        if course in self.grades:
            self.grades[course] = point

    def print_grades(self):
        print(f"{self.name} id: {self.id}, grades are below:")
        for course in self.grades:
            print(f"{course} point is {self.grades[course]}")


zhang = Student("zhangsan", 123)
zhang.set_grade("lang", 99)
zhang.set_grade("math", 98)
zhang.set_grade("eng", 100)
zhang.set_grade("eng2", 100)
zhang.print_grades()
