# Write a function for arithmetic operators(+,-,*,/)
 #Take input from user

a = 13
b = 18
sum = a + b
min = a - b
mul = a * b
div = a / b


print(sum)
print(min)
print(mul)
print(div)

# Write a method for increment and decrement operators(++, --)
# Incremented means the variable value will be incremented by one
a = 5
a+=3
print(a)
b = 12
b-=4
print(b)

# Write a program to find two number equal or not
num1 = input("Enter the number:")
num2 = input("Enter your number:")
if num1==num2:
    print("Two numbers are equal")
else:
    print("Two numbers are not equal")

# Program for relational operators (<,<==, >, >==)

a = 13
b = 16
print(a < b)  #This operator(<) returns True if the left operand is less than the right operand.
print(a <= b) #This operator(<=)returns True if the left operand is less than or equal to the right operand.
print(a > b)  #This operator(>) returns True if the left operand is greater than the right operand.
print(a >= b) #This operator(>=)returns True if the left operand is greater than or equal to the right operand.   
print(a == b) #This operator(==)returns True if both the operands are equal i.e. if both the left and the right operand are equal to each other.
print(a != b) #This operator(!=)returns True if both the operands are not equal.

# Print the smaller and larger number.

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
#To print larger number
if a > b: 
     print(a, "is greater ")
else:
    print(b, " is greater ")
#To print samller number
if a < b:
     print(a, "is smaller ")
else:
    print(b, " is smaller ")         
