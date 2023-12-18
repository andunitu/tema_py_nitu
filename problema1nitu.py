class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary


    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)



#Nitu=> x=4 , x%3=1, Andrei-Bogdan=> y=12; y/3=4;
class Employee:
    emp_count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_employee(self):
        print(f"Employee {self.name}: Salary ${self.salary}")


class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        Manager.mgr_count += 1

    def display_employee(self):
        print(f"Manager {self.name}: Salary ${self.salary}")



manager1 = Manager("Robertel", 60000, "IT")
manager2 = Manager("Bugeac", 70000, "Marketing")
manager3 = Manager("Enqriq", 80000, "HR")
manager4 = Manager("Aphelios", 90000, "Finance")


manager1.display_employee()
manager2.display_employee()
manager3.display_employee()
manager4.display_employee()


employee1 = Employee("Ezreal", 50000)
employee2 = Employee("Diana", 55000)
employee1.display_employee()
employee2.display_employee()

print(f"Employee Count: {employee1.emp_count}")
print(f"Manager Count: {manager1.mgr_count}")
