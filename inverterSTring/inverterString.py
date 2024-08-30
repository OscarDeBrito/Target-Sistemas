
input_string = input("String para inverter: ")
length = len(input_string)
space = ""

for i in range(length):
    
    space += input_string[length - 1 - i]

print("String invertida:", space)
