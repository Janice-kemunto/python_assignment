class Employee: 
  def __init__(self, Name, IDNO, Age, Department):
    self.Name = Name
    self.IDNO = IDNO
    self.Age = Age
    self.Department = Department

  def start(self):
    raise NotImplementedError("Subclass must implement this abstract method")

  def stop(self):
    raise NotImplementedError("Subclass must implement this abstract method")

  class Name(Employee):
    def start(self):
      return f"Manager {self.Name} starts"
    def stop(self):
      return f"Manager {self.Name} stops"

  class IDNO(Employee):
    def start(self):
      return f"Manager {self.IDNO} starts"
    def stop(self):
      return f"Manager {self.IDNO} stops"
  class Age(Employee):
    def start(self):
      return f"Manager {self.Age} starts"
    def stop(self):
      return f"Manager {self.Age} stops"
  class Department(Employee):
    def start(self):
      return f"Manager {self.Department} starts"
    def stop(self):
      return f"Manager {self.Department} stops"
  my_Name = Employee.Name("Janice Kemunto")
  my_IDNO = Employee.IDNO("12345678")
  my_Age = Employee.Age("30")
  my_Department = Employee.Department("Marketing")
  print(my_Name.start())
  print(my_IDNO.start())
  print(my_Age.start())
  print(my_Department.start())

