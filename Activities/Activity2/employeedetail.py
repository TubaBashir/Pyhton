class Employee:
    def __init__(self, emp_id, name, department, role, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.role = role
        self.salary = float(salary)

    def get_details(self):
        """Formats and returns individual employee profile details."""
        return (
            f"🆔 ID         : {self.emp_id}\n"
            f"👤 Name       : {self.name}\n"
            f"🏢 Department : {self.department}\n"
            f"💼 Role       : {self.role}\n"
            f"💵 Salary     : ₹/{self.salary:,.2f}\n"
            f"{'-'*30}"
        )


class EmployeeManagementSystem:
    def __init__(self):
        # Dictionary using unique Employee ID as the key
        self.employees = {}

    def add_employee(self, emp_id, name, department, role, salary):
        if emp_id in self.employees:
            print(f"❌ Error: Employee ID {emp_id} already exists!")
            return False
        
        # Instantiate a new record
        new_emp = Employee(emp_id, name, department, role, salary)
        self.employees[emp_id] = new_emp
        print(f"✅ Employee '{name}' added successfully.")
        return True

    def display_all(self):
        if not self.employees:
            print("📭 No records found in the database.")
            return
            
        print(f"\n{'='*10} ALL EMPLOYEE RECORDS {'='*10}")
        for emp in self.employees.values():
            print(emp.get_details())

    def search_employee(self, emp_id):
        if emp_id in self.employees:
            print(f"\n🔍 Record Found:")
            print(self.employees[emp_id].get_details())
        else:
            print(f"❌ Record with ID {emp_id} not found.")


# --- Simulation Run ---
if __name__ == "__main__":
    # Initialize the system database
    ems = EmployeeManagementSystem()
    
    # 1. Populating dummy records
    ems.add_employee("EMP101", "Arjun Sharma", "Engineering", "Backend Developer", 85000)
    ems.add_employee("EMP102", "Priya Patel", "Human Resources", "HR Manager", 72000)
    ems.add_employee("EMP103", "Rohan Das", "Marketing", "SEO Specialist", 55000)
    
    # 2. Display all data profiles
    ems.display_all()
    
    # 3. Test searching capabilities
    ems.search_employee("EMP102")  # Successful match
    ems.search_employee("EMP999")  # Non-existent search
