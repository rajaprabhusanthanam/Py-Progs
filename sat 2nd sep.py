
#1. Count the number of vowels in a string using a for loop
#where the string is taken as user input

'''
print("Count the number of vowels in a string using a for loop")
print()

count = 0
str1 = ""
str1 = str(input("Enter a String: "))

vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

for j in str1:
    if j in vowels:
        count += 1

print(count)
'''


#2. Print all elements from a list that are divisible by 3 using for loop (given list)

'''
print("2. Print all elements from a list that are divisible by 3 using for loop (list is given)")
print()

list1 = [3,9,20,23,46,40,18,6]
print("the given list:", list1)

for i in list1:
    if i % 3 == 0:
        print(i)
'''


#3. Print the Fibonacci sequence upto n terms using a while loop- user input

'''
print("3. Print the Fibonacci sequence upto n terms using a while loop(n - user input)")
print()

n = int(input("enter a number: "))

a = 0
b = 1

print("fib", a, b, end = " ")

for i in range(2, n):
    c = a  + b
    a = b
    b = c
    print(c, end= " ")

print()
'''

#4. Find the max num in a given using a for loop

'''
print("4. Find the max num in a given using a for loop")
print()

list1 = [10,20,30,40,50,15,25,35,45]

max1 = list1[0]

for i in list1:
    if i > max1:
        max1 = i

print("The maximum number in a given list is:", max1)
'''

#5. find the product of its elements of a given list using a loop

'''
print("5. find the product of its elements of a given list using a loop")
print()

list1 = [1,10,2,9,3,8,4,7,5,6]

product = 1

for i in list1:
    product *= i

print("The product of the list elements is:", product)
'''

#6. print the ASCII value of all the characters from a-z using for loop

'''
print("6. print the ASCII value of all the characters from a-z using for loop")
print()

import string

atoz = string.ascii_letters
print("a to z and A to Z")
print(atoz)

for i in atoz:
    print(ord(i))
'''

#7. print the square of numbers from 1 to n(user input) using a while loop 

'''
print("7. print the square of numbers from 1 to n(user input) using a while loop")
print()

n = int(input("Enter a number: "))

start = 0

while start < n:
    square = i ** 2
    start += 1
    print("the number is:", i)
    print("and the square of the number is:", square)
'''

#8. find the second smallest no in a given list

'''
print("8.find the second smallest no in a given list")
print()

list0 = [10,20,30,40,50,15,25,35,45]

list1 = set(list0)
list1.remove(min(list1))

list2 = list(list1)


min1 = list2[0]

for i in list2:
    if i < min1:
        min1 = i

print("the second smallest no is:", min1)
'''

#9. Print the uppercase equivalent of all the characters in a input string using for loop

'''
print("9. Print the uppercase equivalent of all the characters in a input string using for loop")
print()

str1 = input("Enter a string: ")
str2 = ''

for i in str1:
    if( i >= 'a' and i <= 'z'):
        str2= str2 + chr((ord(i) - 32))
    else:
        str2 = str2 + i
 
print("The Entered string is:", str1)
print("The Uppercase Equivalent is:", str2)
'''

#10.Given a list of strings, concatenate them to form a single sentence using a for loop

'''
print("10.Given a list of strings, concatenate them to form a single sentence using a for loop")
print()

str1 = ['raja', 'prabhu', 'santhanam', 'ramasamy']
str2 = ""

for i in str1:
    str2 += i

print(str2)
'''

#11. find the sum of the digits of a number using a while loop

'''
num = int(input("Please enter digits: "))
sum = 0

while (num > 0):
    rem = num % 10
    sum = sum + rem
    num = num // 10

print(sum)
'''

#12. determine the prime numbers between 1 and n using a nested for loop with n is user input

'''
print("12. determine the prime numbers between 1 and n using a nested for loop with n is user input")
print()

n = int(input("Enter a number: "))

for i in range(2, n+1):
    for j in range(2, n+1):
        if i % j == 0:
            break
    if i == j:
        print(i, end= ",")
'''

#13. given a list of numbers, count occurences of a specific number using for loop

'''
print("13. given a list of numbers, count occurences of a specific number using for loop")
print()

list1 = [1,11,1,12,1,13,2,11,2,12,2,13,3,13,4,14]
print(list1)

n = int(input("Enter the number to find out count: "))

occ = 0

for i in list1:
    if i == n:
        occ = occ + 1
print("the counted occurances of the given number is:", occ)
'''

#14. in a given list find the largest string using for loop

'''
print("14. in a given list find the largest string using for loop")
print()

list1 = ['rajaprabhu', 'arun', 'akash', 'parvati', 'vijay', 'rathnavel']

large = -1

for i in list1:
    if len(i) > large:
        large = len(i)
        largestr = i
print("The Longest string is: ", largestr)
'''

#15. reverse a given list using a while loop

'''
print("15. reverse a given list using a while loop")
print()

list1 = ['rajaprabhu', 'arun', 'akash', 'parvati', 'vijay', 'rathnavel']

start = 0
end = len(list1) -1

while start < end:
    list1[start], list1[end] = list1[end], list1[start]
    start += 1
    end -= 1
print(list1)
'''
