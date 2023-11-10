class person:
  name=""
  def __init__(self,name):
    self.name = name
  def getinfo(self):
    print("this person's name is ",self.name)

class student(person):
  nis = ""
  def __init__(self, name, nis):
    super().__init__(name)
    self.nis = nis

  def getinfo(self):
    print("this student's name is ",self.name)

  def study(self,subject):
    print("this student is studying",subject)

class docter(person):
  reg_number=""
  def __init__(self, name, reg_number):
    self.name=name
    self.reg_number=reg_number

  def getinfo(self):
    print("this docter's name is ",self.name)

  def reg(self):
    print("this docter's reg number is ",self.reg_number)

  def diagnose(self,patient):
    print("this docter is diagnosing",patient)

  def treat(self,patient):
    print("this docter is treating",patient)

person = person("ahmad")
person.getinfo()

student = student("bambang","4614613466")
student.getinfo()
student.study("Math")

docter = docter("Diluc","23434619436")
docter.getinfo()
docter.reg()
docter.diagnose("mamang")
docter.treat("mamang")