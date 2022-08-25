#Write a program to print "Bright IT Carrer" ten times usinh for loops
name = "Bright IT Carrer"
for i in range (10):
    print(name)


# Write a program to print 1 to 20 numbers using the while loop
i=1
while (i<=20):
    print(i)
    i=i+1

#Program to equal operator and not equal operator

a = 7
b = 10
print(a==b)
print(a!=b)

#Write a program to print odd and even number
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number:"))
if num%2==0:
    print("Number is Even")
else:
    print("Number is odd")

# Write a program to print largest number among three numbers.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
num3 = int(input("Enter a number:"))

if (num1>num2) & (num1>num3):
    print("Largest number is:",num1)
elif (num2>num1 & num2>num3):
    print("Largest number is:",num2)
else:
    print("Largest number is:",num3)

# Write a program to print even number between 10 and 20 using while.

a = 10
b = 20
print("Even Numbers Between 10 to 20: ",end=" ")
while a <= b:
    if(a % 2 == 0):
        print("{0}".format(a),end=" ")
    a = a + 1
print()

# Write a program to print 1 to 10 usig the do-while loop statement.

a = 1
print("Print 1 to 10 using the do-while loop statement:",end=" ")
while True:
    print(a,end=" ")
    a = a + 1
    if(a > 10):
        break 
print()

# Write a program to find Armstrong number or not.

a = int(input('Enter a number to check if its armstrong or not: '))
sum = 0
temp = 0
temp = a
while temp > 0:
    r = temp % 10
    sum += r ** 3
    temp //= 10
if a == sum:
    print(a," is an amstrong number")
else:
    print(a," is not an amstrong number")

# Write a program to find the prime or not.

number = int(input("Enter any number to check prime number or not: "))
if number > 1:                          # prime number is always greater than 1
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
        else:
           print(number, "is a prime number")
# if the entered number is less than or equal to 1
# then it is not prime number
else:          
    print(number, "is not a prime number")

    
# Write a program to palindrome or not.
num = int(input("Enter a number to check polindrom or not:"))
temp = num
reverse_number = 0
while(num>0):
    digit = num % 10
    reverse_number = reverse_number*10+digit
    num = num//10
    if(temp==reverse_number):
        print("The number is polindrom")
    else:
        print("The number is not a polindrom")
    

# Program to check whether a number is EVEN or ODD Using Switch
a = int(input('Enter Number to check is EVEN or ODD: '))
if a % 2 == 0:
    print(a,"is Even")
else:
    print(a,"is odd")  



