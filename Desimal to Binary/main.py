print("Desimal to Binary Calculator")
print("============================")

desimal = int(input("masukkan angka Desimal :"))

to_binary= bin(desimal).replace("0b","")

print(f"{desimal} = {to_binary}")
