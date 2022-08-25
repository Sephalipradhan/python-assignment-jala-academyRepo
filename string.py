#Different ways creating a string
#First ways
string = "sefali"
print(string)
#2nd ways
print("sefali")
# 3rd ways
a = 'sefali'
print(a)
#4th way
a = '''shila'''
print(a)
#5th way
a = """sefali"""
print(a)

#Concatinating two strings using + operator
a = "sefali"
b = "pradhan"
print(a+b)

#Print length of the string
a = "shila"
print(len(a))


str1 = "sefali"
str2 = "pradhan"
str3 = "fa"
print("position of fa:",str1.index(str3))
#Comparing two strings
str1 = "sefali"
str2 = "sefali pradhan"
print(str1==str2)
print(str1!=str2)
#startswith(),endwith()
str1 = "sefali pradhan"
str2 = "sunanda pradhan"
print(str1.startswith("sefali"))
print(str2.endswith("han"))

#Trimming strings with strip()
str1 = "Hello I am sefali"
print(str1.strip("am"))
print()

#Replacing characters in string with replace()

str1 = "shila"
print(str1.replace("shila","pradhan"))

#Splitting string with split()
str1 = "Hi-sefali-pradhan"
print(str1.split("-")) 
print()
# Converting integers object to string
num = 10
num1 = str(num)
print(num1)
print(type(num1))

#converting to uppercase and lowercase
str1 = "shila"
str2 = "Pradhan"
print(str1.upper())
print(str2.lower())


