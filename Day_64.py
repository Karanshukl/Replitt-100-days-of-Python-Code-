class job:
  def __init__(self, name, salary,hourswork):
    self.name = name
    self.salary = salary
    self.hourswork = hourswork

  def prettyPrint(self):
    print(f"Name: {self.name}\nSalary: {self.salary}\nHourswork: {self.hourswork}")

class doctor(job):
  def __init__(self,name, salary, hourswork, speciality, experience):
   super().__init__(name, salary, hourswork)
   self.speciality  = speciality
   self.experience =experience

  def prettyPrint(self):
    print(f"Name: {self.name}\nSalary: {self.salary}\nHourswork: {self.hourswork}\nSpeciality: {self.speciality}\nYears of Experience: {self.experience}")

  
class teacher(job):
  def __init__(self,name, salary, hourswork, subject, position):
   super().__init__(name, salary, hourswork)
   self.subject  = subject
   self.position = position

  def prettyPrint(self):
    print(f"Name: {self.name}\nSalary: {self.salary}\nHourswork: {self.hourswork}\nSubject: {self.subject}\nPosition: {self.position}")



it = job("Carlos","100k",2) 
it.prettyPrint()
print()
cs = teacher("Hradesh","30k",8,"DSA","Junior")
cs.prettyPrint()
print()
dr = doctor("Dr. Karan","150k",9,"Brain",12)
dr.prettyPrint()
  
