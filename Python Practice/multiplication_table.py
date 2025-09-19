input_number = int(input(f"Enter the multiplication table number:  ")) 
print(f"Multiplication table for {input_number} is shown below:")
for i in range(1,11):
    multiply=input_number*i
    print(f"{input_number}*{i} = {multiply}")
