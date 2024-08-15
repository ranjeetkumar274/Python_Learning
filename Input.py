# learning of using input()

x = input()
print(x)

print(type(x))

#program to add two numbers

print("Enter your first number : ") 
x = input() 
print("Enter your second number : ")
y = input()

print("Your answer is : ")
z = int(x)+int(y)   #here  we have to use typeconversion because input function can only return string values
print(z)