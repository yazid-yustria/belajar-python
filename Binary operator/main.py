print("binary operator")
print("~~~~~~~~~~~~~~~")

num1 = int(input("Ketik Angka pertama :"))
num2 = int(input("Ketik Angka Kedua :"))

and_operator= num1 & num2
or_operator= num1 | num2
xor_operator= num1 ^ num2
not_operator1= ~ num1
not_operator2= ~ num2

print(f"{num1} & {num2} = {and_operator}")
print(f"{num1} | {num2} = {or_operator}")
print(f"{num1} ^ {num2} = {xor_operator}")
print(f"{num1} = {not_operator1}")
print(f"{num2} = {not_operator2}")
