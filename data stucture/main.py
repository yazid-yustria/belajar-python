#data struture

#list data
#square blaket/multiple data/can be modified
students = ["Ahmad","Beni","Cyno","Dori"]
print(type(students)) #check data type
print(students[2])
students.append("Benny") # add new data
students[1]="Fichl" #replace data
students.remove("Ahmad") #remove data by name
students.pop(2) #remove data by order/number
print(students)
students.clear() #clear all data
print(students)

#tuple data
#round blaket/cannot be modified
fruit= ("apple","blueberry","cherry","grape","starfruit","grape")
print(type(fruit)) #check data type
print(fruit[2])
#fruit.append("jackfruit") # add new data(error)
#tuple can be modified by change it to list
fruit_list=list(fruit)
fruit_list.append("jackfruit")
fruit_list.remove("jackfruit")
fruit_list[2]="Melon"
fruit_list.pop(0)
fruit=tuple(fruit_list)
print(fruit)

#set data
#Kurung kurawal/tdk berurut/tdk bisa di edit/tdk bisa memliki data yg sama
mobil={"Honda","Toyota","Daihatsu","Mitsubitsi","Ford","Suzuki"}
print(type(mobil)) #check data type
print(mobil)
#set data Cannot be access
#print(mobil[2]) #erro
mobil.add("Tesla")
mobil.add("Ferrari")
mobil.discard("Wuling")#not show error if the item not found
#mobil.remove("Wuling") #show error if the item not found
mobil.pop()#remove random data
print(mobil)

#Dictionory data
#kurung kurawa/key value
# Dictionary

car = {
  "model" : "truck",
  "brand" : "ford",
  "elctric" : False,
  "year" : 2010,
  "price" : 1400000000,
  "color choices" : ["red", "blue", "black"]
}

# accessing value
print(car['brand'])
print(car['price'])

# modify
car['year'] = 2015

# add new key:value
car['max speed'] = 300

# remove key:value
# using .pop()
car.pop("model")

# using .popitem()
# remove last item
car.popitem()
print(car)