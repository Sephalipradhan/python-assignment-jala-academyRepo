#Write a program to print your name
print("sefali pradhan")

#Write a program for a single-line comment and multi-line comment

#Comments in python means for understanding purpose.It ignored by the interpreter at the time of execution..
#Python uses two types of comments 
# 1.single line comments
# 2.Multi-line comments
# Single-line comments are used for single line & multi-line comments are used for multiple line
# symbol used for single-line comments & ''' symbol used for multi-line coments.

# Write a program for which programming language is your favourite

#print("My favourite programming language is python")   # Ex. of single line comment

# Print your all favourite subject one by one
'''print("python")
   print("java")
   print("kotlin")           example of multi-line comment
   print("Php")'''

#Write a program to Define variables for different Data Types int, Boolean, char, float, double and print on the Console. 
a = 96
print(type(a))

b = "Sefali pradhan"
print(type(b))

c = 34.78
print(type(c))

d = True
print(type(d))

# Define the local and Global variables with the same name and print both variables and understand the scope of the variables.

a = 5

# Uses global because there is no local 'a'

def f():

    print('Inside f() : ', a)

# Variable 'a' is redefined as a local

def g():

    a = 2

    print('Inside g() : ', a) 

# Uses global keyword to modify global 'a'

def h():

    global a

    a = 4      #Value of 'a' modified

    print('Inside h() : ', a)  

# Global scope

print('global : ', a)

f()

print('global : ', a)

g()

print('global : ', a)

h()