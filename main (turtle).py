#import semua fuction turtle
from turtle import * 

getscreen()

bgcolor("red")
pencolor("purple")
pensize(4)
#Shape("") buat bentuk
#penup buat bergerak tanpa menulis
fillcolor("black")#buat ngisi
begin_fill()

speed(10)

init_size=40

for b in range(4):
  for i in range(12):
    forward(init_size)
    left(50)
  for a in range(12):
    backward(init_size)
    right(50)
  left(30)
  init_size=init_size+2
end_fill()
#sepasang dgn begin fill
    
  

#init_size=5

#for i in range(4):
#  for a in range(init_size):
#    forward(init_size)
#    right(90)
#  init_size+=10

#for r in range(3):
#  forward(20)
#  left(180/3)


done()