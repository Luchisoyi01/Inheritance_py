class person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname
    
  def printname(self):
    print(self.firstname, self.lastname)

class Student(person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("watson", "Luchisoyi", 2025)
x.welcome()