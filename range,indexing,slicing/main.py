#range(start,stop,step)
#range(stop) Way1
#range(start,stop) Way2
#range(start,stop,step) Way3

num_list1 = list(range(97))
print(num_list1)

num_list2 = list(range(19,86))
print(num_list2)

num_list3= list(range(2,12,3))
print(num_list3)

#indexing
num_list=list(range(1,101))

#mengambil dari kiri
print(num_list[5])

#mengambil dari kiri
print(num_list[-1])
print(num_list[-4])

#slicing

#list[stop]
#list[start:stop]
#list[start:stop:step]

num_list=list(range(10,101,5))
print(num_list[:4])
print(num_list[3:9])
print(num_list[2:8:2])