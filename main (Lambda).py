#def sayhello(name)
#  print("Selamat Datang", name)

sayhello = lambda name:print("Selamat Datang", name)

sayhello("yoyo")

#def additional(num1,num2)
#  result = num1 + num2
#  print (result)

additional = lambda num1,num2 : print (num1+num2)
additional(30,40)






#lambda tanpa argumen
(lambda : print ("selamat datang"))()

#lambda dengan argumen
(lambda fruit : print ("saya suka", fruit))("kurma")

#lambda dengan default argumen
(lambda name="" : print ("Selamat datang",name))()

