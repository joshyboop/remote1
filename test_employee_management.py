import unittest
import employee_management

# Then the structure of a test should loosely follow this workflow:
# 1. Create your inputs
# 2. Execute the code being tested, capturing the output
# 3. Compare the output with an expected result

class TestEmployeeManagement(unittest.TestCase):
    # CREATE EMPLOYEE
    def test_create_employee(self):
        management = employee_management.EmployeeManagement()
        emp = employee_management.Employee("John", 23, 600, "Liberal Arts")
        management.create_employee(emp)
        self.assertIn(emp, management.employees)

    # CREATE EMPLOYEE WITH SAME ID
    def test_create_employee_DUPLICATE(self):
        management = employee_management.EmployeeManagement()

        emp = employee_management.Employee("John", 23, 600, "Liberal Arts")
        emp1 = employee_management.Employee("Freddie", 29, 600, "Chemical Engineering")

        management.create_employee(emp)
        management.create_employee(emp1)

        self.assertNotIn(emp1, management.employees)

    # CREATE EMPLOYEE WITH MISSING ATTRIBUTES
    def test_create_employee_MISSING(self):
        management = employee_management.EmployeeManagement()
        emp = employee_management.Employee("John", None, None, "Liberal Arts")
        management.create_employee(emp)
        self.assertNotIn(emp, management.employees)

    # CREATE EMPLOYEE WITH STRING AS AGE
    def test_create_employee_STRING_AGE(self):
        management = employee_management.EmployeeManagement()
        emp = employee_management.Employee("John", "23", 600, "Liberal Arts")
        management.create_employee(emp)
        self.assertNotIn(emp, management.employees)

    # CREATE EMPLOYEE WITH NEGATIVE VALUES (AGE)
    def test_create_employee_NEGATIVE_AGE(self):
        management = employee_management.EmployeeManagement()
        emp = employee_management.Employee("John", -23, 600, "Liberal Arts")
        management.create_employee(emp)
        self.assertNotIn(emp, management.employees)

    # CREATE EMPLOYEE WITH NEGATIVE VALUES (ID)
    def test_create_employee_NEGATIVE_ID(self):
        management = employee_management.EmployeeManagement()
        emp = employee_management.Employee("John", 23, -600, "Liberal Arts")
        management.create_employee(emp)
        self.assertNotIn(emp, management.employees)

    # GET EMPLOYEE BY ID
    def test_get_employee_by_id(self):
        management = employee_management.EmployeeManagement()

        emp1 = employee_management.Employee("Paul", 25, 601, "Culinary Arts")
        emp2 = employee_management.Employee("Ringo", 21, 602, "Literature")
        emp3 = employee_management.Employee("George", 20, 603, "Astrophysics")

        management.create_employee(emp1)
        management.create_employee(emp2)
        management.create_employee(emp3)

        self.assertEqual(emp2, management.get_employee_by_id(602))

    # GET EMPLOYEE BY ID THAT DOES NOT EXIST
    def test_get_employee_by_id_DOES_NOT_EXIST(self):
        management = employee_management.EmployeeManagement()

        emp1 = employee_management.Employee("Paul", 25, 601, "Culinary Arts")
        emp2 = employee_management.Employee("Ringo", 21, 602, "Literature")
        emp3 = employee_management.Employee("George", 20, 603, "Astrophysics")

        management.create_employee(emp1)
        management.create_employee(emp2)
        management.create_employee(emp3)

        self.assertEqual(None, management.get_employee_by_id(700))

    # DELETE EMPLOYEE BY ID
    def test_delete_employee_by_id(self):
        management = employee_management.EmployeeManagement()

        emp1 = employee_management.Employee("Paul", 25, 601, "Culinary Arts")
        emp2 = employee_management.Employee("Ringo", 21, 602, "Literature")
        emp3 = employee_management.Employee("George", 20, 603, "Astrophysics")

        management.create_employee(emp1)
        management.create_employee(emp2)
        management.create_employee(emp3)

        management.delete_employee_by_id(601)
        self.assertNotIn(emp1, management.employees)

    # DELETE EMPLOYEE BY ID THAT DOES NOT EXIST
    def test_delete_employee_by_id(self):
        management = employee_management.EmployeeManagement()

        emp1 = employee_management.Employee("Paul", 25, 601, "Culinary Arts")
        emp2 = employee_management.Employee("Ringo", 21, 602, "Literature")
        emp3 = employee_management.Employee("George", 20, 603, "Astrophysics")

        management.create_employee(emp1)
        management.create_employee(emp2)
        management.create_employee(emp3)

        management.delete_employee_by_id(700)
        self.assertIn(emp1, management.employees)

    # GET EMPLOYEE AFTER DELETING
    def test_get_employee_by_id_AFTER_DELETING(self):
        management = employee_management.EmployeeManagement()

        emp1 = employee_management.Employee("Paul", 25, 601, "Culinary Arts")
        emp2 = employee_management.Employee("Ringo", 21, 602, "Literature")
        emp3 = employee_management.Employee("George", 20, 603, "Astrophysics")

        management.create_employee(emp1)
        management.create_employee(emp2)
        management.create_employee(emp3)

        management.delete_employee_by_id(603)

        self.assertEqual(None, management.get_employee_by_id(603))

if __name__ == "__main__":
     unittest.main()