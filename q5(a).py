class employee():
    def show_data(self):
        return f"Name of employee is {self.name} and salary is {self.salary}"
    def __del__(self):
        return

emp1=employee()
emp2=employee()
emp3=employee()

emp1.name="Mehak"
emp1.salary="40000"

emp2.name="Ashok"
emp2.salary="50000"

emp3.name="Viren"
emp3.salary="60000"

print("Before changing value of salary:")
print(emp1.show_data())

emp1.salary="70000"

print("After changing value of salary:")
print(emp1.show_data())
