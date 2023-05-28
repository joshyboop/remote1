class Employee:
    def __init__(self, name, age, id, department):
        self.name = name
        self.age = age
        self.id = id
        self.department = department

class EmployeeManagement:
    def __init__(self):
        self.employees = []

    # Create a new employee with the following details: name:string, age:int, id:int, department:string
    def create_employee(self, my_employee):
        if my_employee.name == None or my_employee.age == None or my_employee.id == None or my_employee.department == None or type(my_employee.age) != int or my_employee.age < 0 or my_employee.id < 0:
            return
        
        for employee in self.employees:
            if employee.id == my_employee.id:
                return
            
        self.employees.append(my_employee)
    
    # Retrieve employee information by id
    def get_employee_by_id(self, id):
        for employee in self.employees:
            if employee.id == id:
                return employee

    # Delete an employee given his id
    def delete_employee_by_id(self, id):
        for i in range(len(self.employees)):
            if self.employees[i].id == id:
                del self.employees[i]
                break

# After you implement the program, you make some Exploratory Testing to make sure it is working.
# emp = Employee("John", 23, 600, "Liberal Arts")
# emp1 = Employee("Paul", 25, 601, "Culinary Arts")
# emp2 = Employee("Ringo", 21, 602, "Literature")
# emp3 = Employee("George", 20, 603, "Astrophysics")

# emp_manager = EmployeeManagement()

# emp_manager.create_employee(emp)
# emp_manager.create_employee(emp1)
# emp_manager.create_employee(emp2)
# emp_manager.create_employee(emp3)

# print(vars(emp_manager.get_employee_by_id(602)))
# emp_manager.delete_employee_by_id(602)