class Animal:
  name = "" #properti/attribute
  color = ""

  def __init__(self, Animal_name, Animal_color): #constructor
    self.name= Animal_name
    self.color= Animal_color
  
  #def makesound(self,sound):
    #print("animal in making sound",sound)

  #def eat(self,food):
    #print("animal is eating",food)

  #def sleep(self):
    #print("animal is sleeping")

  def makesound(self,sound):
    print(f"{self.name} is {sound}")

  def eat(self,food):
    print(f"{self.name} is eating {food}")

  def sleep(self):
    print(f"{self.name} is sleeping")

cat = Animal("Bravo","White")
cat.makesound("meaw")
cat.sleep()
cat.eat("fish")

