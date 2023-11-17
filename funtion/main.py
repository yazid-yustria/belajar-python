def tambah(firstnum,secondnum):
  tambah=firstnum + secondnum
  print(f"{firstnum} + {secondnum} = {tambah}")
  
def kurang(firstnum,secondnum):
  kurang=firstnum - secondnum
  print(f"{firstnum} - {secondnum} = {kurang}")

def kali(firstnum,secondnum):
  kali=firstnum * secondnum
  print(f"{firstnum} X {secondnum} = {kali}")

def bagi(firstnum,secondnum):
  bagi=firstnum / secondnum
  print(f"{firstnum} : {secondnum} = {bagi}")




print("KALKULATOR SEDERHANA")
print("vvvvvvvvvvvvvvvvvvvv")
print("MODE KALKULATOR")
print("1)TAMBAH")
print("2)KURANG")
print("3)KALI")
print("4)BAGI")

mode =int(input("pilih 1/2/3/4:"))

firstnum =int(input("angka pertama:"))
secondnum =int(input("angka kedua:"))

if mode == 1:
  tambah(firstnum,secondnum)
elif mode == 2:
  kurang(firstnum,secondnum)
elif mode == 3:
  kali(firstnum,secondnum)
elif mode == 4:
  bagi(firstnum,secondnum)
else :
  print("mode yg dipilih salah")

  