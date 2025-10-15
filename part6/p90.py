from abc import ABC,abstractmethod
class employee(ABC):
    @abstractmethod
    def salary(self):
        pass
    def details(self):
        print("Details of employee")
    
class manager(employee):
    def salary(self):
        print("Salary calculation of manager")
    def team(self):
        print("Display team members")

class staff(employee):
    def details(self):
        print("Employee details")
    def salary(self):
        print("Salary calculation of staff")
    def greet(self):
        print("Staff method")

m = manager()
m.team()
m.salary()
m.details()
s=staff()
s.details()
# s.greet()
# s.salary()