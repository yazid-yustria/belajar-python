print("MY TO DO LIST")
print("VVVVVVVVVVVVV")

active = True

while active :
  todo = input("Apa Yang Ingin Kamu Lakukan? ")
  file = open('To Do list,txt','a')
  file.write(todo+"\n")
  file.close()

  file = open('To Do list,txt','r')
  print(file.read())

  active = input("ingin melanjutkan? y/n")