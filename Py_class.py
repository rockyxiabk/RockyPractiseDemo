class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def printCount(self):
        print("employee count:", Employee.empCount)

    def printEmployee(self):
        print("employee info: name:", self.name, "   salary:", self.salary)


if __name__ == '__main__':
    employee1 = Employee("jack", 5000)
    employee2 = Employee("rocky", 10000)
    employee1.printEmployee()
    employee2.printEmployee()
    print("employee Count:", Employee.empCount)
