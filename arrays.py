# Write a function to add integer values of an array
arr=[]
arr=[10,20,30,40,50]
b = sum(arr)
print('sum of the array is:',b)

#Write a function to calculate the average value of an array of integers
def cal_average(num):
    sum_num = 0
    #Loop through the array to average value of elements 
    for i in num:
        sum_num = sum_num + i          
    avg = sum_num / len(num)
    return avg
print("The average is", cal_average([10,21,32,43,54]))

#WAP to find the index of array elements
a = [10,20,30,40,50]
print(a[0])   #Index of an array always starts from zero 
print(a[1])
print(a[2])
print(a[3])
print(a[4])
a = [10,20,30,40,50,2,3]

#printing element at specific index in array
index = a.index(10)
print("Index of 10: ",index)

index = a.index(20)
print("Index of 20: ",index)

index = a.index(30)
print("Index of 30: ",index)

index = a.index(40)
print("Index of 40: ",index)

index = a.index(50)
print("Index of 50: ",index)

index = a.index(3)
print("Index of 3: ",index)

index = a.index(2)
print("Index of 2: ",index)
# Write a method to verify if the array contains two specified elements (12,23)

#Initialize array
arr = [1,2,3,4,5,6,7,8,12,23]
#Loop through array to test if array contains a specific value
for i in arr:
    if i == 12:
        print("Element exist")
    

# Write a function to remove a specific element from an array.
#Initialize array
arr = [40,45,35,30,67]

#removing a specific element from an array
arr.remove(67)
print(arr)

#WAF to copy an array to another array
arr1= ['sefali','priyanka','barsha','adyasha']
arr2 = arr1.copy()
print(arr2)

#WAF to insert an element at a specific position in an array

a = [100,300,400,450]
a.insert(4,900)
print(a)

#WAF to find the minimun & maximum values of an array
arr = [12,13,14,15,16]
print("maximum values in an array is:",max(arr))  #Getting maximum values
print("minimum values in an array is:",min(arr)) # Getting minimum values 

#WAF to reverse an array of integer values.

arr = ['apple','orange','mango','strawberry']
arr.reverse()
print(arr)

#WAF to find the duplicate values of an array

#Initialize array    
arr = [21,11,31,13,11]
#Using loop to check duplicate values in array
for i in range(0,len(arr)):
    for k in range(i + 1,len(arr)):
        if arr[i] == arr[k]:
            print("Duplicate element in given array:",arr[k])

# WAP to find out the common values between two arrays
arr = [0,1,2,3,4,5]
arr1 = [0,2,6,7,8,9]
print("Common values in given arrays are:",set(arr).intersection(arr1))

# Write a method to remove duplicate elements from an array.
#Initialize array
arr = [11,22,33,11,44,55]
a = [] #empty array
#Using loop to remove duplicated elements
for i in arr:
    if i not in a :
        a.append(i)
print(a)

# Write a method to find the second largest number in an array.

#Initialize array
arr = [108,102,103,104,105,106,107]
arr.sort() #Sorting in ascending order. 
print("Second largest number:",arr[-2]) 

# Write a method to find number of even number and odd numbers in an array.

#Initialize array
arr = [1,2,3,4,5,6,7,8,9]
even_numbers = 0
odd_numbers = 0
#using loop to find even and odd numbers in array
for i in arr:
    if i % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1 
print("Even Numbers in given array:",even_numbers)
print("Odd Numbers in given array:",odd_numbers)

#Write a function to get the difference of largest and smallest value.

#Initialize array
arr = [10,6,11,13,14]
arr.sort() #Sorting in ascending order
print("Diffrence of largest and smallest value:",arr[4]-arr[0])

# Write a method to verify if the array contains two specified elements(12,23).

#Initialize array
arr = [1,12,19,23,33,54]
#using loop to find if array contains specific elements
for i in arr:
    if i == 12:
        print("Exist in array")
    if i == 23:
        print("Exist in array")






