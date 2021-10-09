# #print("NUM")
# #3num = int(input("Enter rows"))
# #3bool == "1"
# #if bool
# #3for i in range(0,num+1):
#  #   print("*"*i)
#
#
# #more on files
#
# #f = open("CHAITANYA 2.txt")
# #print(f.tell())
# #print(f.readline())
# #print(f.tell())
# #f.seek((0))
# #print(f.readline())
# #print(f.tell())
# #f.close()
#
# # with open("CHAITANYA 2.txt") as f:
# #     a = f.readlines()
# #     print(a)
# #
# # f = open("CHAITANYA 2.txt", "rt")
# # print(f.read())
#
# #Health Management System
# # 3. Clients - Harry, Rohan and Hammad
# # def getdate():
# #     import datetime
# #     return datetime.datetime.now()
#
#
# print("WHOSE HISTORY DO YOU WANT TO KNOW\n"
#       "PRESS 1 FOR HARRY\n"
#       "PRESS 2 FOR ROHAN\n"
#       "PRESS 3 FOR HAMMAD\n")
# a = input()
# if int(a) == 1:
#       f = open("Harry")
#       print("WHAT DO YOU WANT TO DO?\n"
#             "VIEW LOG PRESS 1\n"
#             "ENTER LOG PRESS 2\n")
#       h = input()
#       if int(h) == 1:
#             f = open("Harry", "rt")
#             print("FOR WHENCE DO YOU WANT TO SEE LOG OF?\n"
#             "PRESS 1 FOR MORNING\n"
#             "PRESS 2 FOR AFTERNOON\n"
#             "PRESS 3 FOR EVENING SNACK\n"
#             "PRESS 4 FOR DINNER\n")
#             h1 = input()
#             if int(h1) == 1:
#                   print(f.read(28))
#
# # elif int(a) == 2:
# #       f = open("Rohan.txt")
# # elif int(a) == 3:
# #       f = open("Hammad.txt")
#
#
#
#
#
#
# print("WHAT DO YOU WANT TO DO?"
#       "FRO VIEWING LOG PRESS 1"
#       "FOR INPUT PRESS 2")
# r = input()
# if int(r) == 1:
#       f = open("Rohan.txt", "rt")
#
#

#print('cow', 'dog', 'milk', sep=',', end='!!!\n')

# print('This is my first programme')
# print('Using python script mode')
# print('Its advantageous over interactive mode')
# print('it saves the statements typed using this mode')

# x = 3 + 4j
# y = 4 - 3j
#
# print(x + y)

# print("Je t'aime, " * 5)

# print("What is your name?")
# input()
# print("Enter 1st number..")
# a = input()
# print("Enter 2nd number..")
# b = input()
# print("Which operator do you want to use?? \n "
#       "1. ADDITION. \n"
#       "2. SUBTRACTION. \n"
#       "3. MULTIPLICATION. \n"
#       "4. DIVISION. ")
# c = input()
#
# if int(c) == 1:
#     print("Your answer is= ", float(a) + float(b))
# elif int(c) == 2:
#     if int(a) >= int(b):
#         print("Your answer is =", float(a) - float(b))
#     elif int(b) >= int(a):
#         print("Your answer is =", float(b) - float(a))
# elif int(c) == 3:
#     print("Your answer is =", float(a) * float(b))
# elif int(c) == 4:
#     print("Your answer is =", float(a) / float(b))

# def triangle():
#     print("*")
#     print("**")
#     print("***")
#     print("****")
#
#
# def arearectangle(l, b):
#     area = l*b
#     return area

# print("ENTER YOUR NUMBER")
# a = input()
# if int(a)%2 == 0:
#     print("EVEN")
# else: print('ODD')

# print("ENTER ANY NUMBER")
# a = input()
# if int(a) > 0:
#     print("POSITIVE NUMBER")
# elif int(a) == 0:
#     print("ZERO")
# elif int(a) < 0:
#     print("NEGATIVE NUMBER")

# for i in range(0,12,2):
#     print('HELLO',i,"WORLD")
#
# count = 1
# while count <= 5:
#     print(count)
#     count += 1.3


# i = 2
# while ( i>=0 ):
#     j = 2
#     while (j >= 0):
#         print(2,end=" ")
#         j = j-1
#     print()
#     i = i-1

# a = 157
# print(a)
#
# for letter in "PYTHON":
#     print(letter)
#
# numbers = (1, 2, 3, 4, 5 ,6, 7, 8, 9, 10)
# for n in numbers:
#     if n%2 == 0:
#         print(n, 'is an even number')
#     else: print(n, 'is an odd number')
#
# count = 1
# while count <= 50:
#     print(count)
#     count += 2

# i = 2
# while (i >= 0):
#     j = 1
#     while (j>=0):
#         print (2, end=" ")
#         j = j-1
#     print()
#     i = i-1

# for val in 'string':
#     if val == "i":
#         break
#     print(val)
# else:
#     print ("Bye")
#
# for x in range (5,10,2):
#     print(x)

# m1 = int(input("ENTER MARKS OF MATHS"))
# m2 = int(input("ENTER MARKS OF ENGLISH"))
# m3 = int(input("ENTER MARKS OF PHYSICAL EDUCATION"))
# m4 = int(input("ENTER MARKS OF PHYSICS"))
# m5 = int(input("ENTER MARKS OF CHEMISTRY"))
# grade = (m1+m2+m3+m4+m5)/5
# if grade>50:
#     print("PASS")
#     print("PASS PERCENTAGE ",grade,"%")
# else: print("FAIL")

# print("there is no \"well\"")

# var1 = "HELLO WORLD"
# print(var1[0])
# print(var1[-])

# str= "COMPUTER SCIENCE"
# for i in str:
#     print(i) #for printing all the letters in consecutive lines

# str1 = 'welcome'
# str1.capitalize()

# str1 ='cold coffee '
# print(str1.replace('cold','hot'))
# b = str1*3
# print(b)


# x = int(input("ENTER THE NUMBER WHICH YOU WAN TABLE OF"))
# i = 1
# while(i<=20):
#     print(x, "x", i, "=", x*i)
#     i += 1

# x = float(input('ENTER VALUE OF x:'))
# y = int(input("ENTER LIMIT:"))
# s = 0
# # for i in range (0,n+1):
# #     fact=1
# #     for k in range (1,k+1):
# #         fact=fact*k
# #     s+=(-x**i)/fact(i)
# # print(s)
#
# # x = ('python')
# # print('o' in x)
# # print('l' in x)
# #
# # x = ("THERE IS A SMALL DOSSIER")
# # print(x[1:22:2])
# # print(len(x))
# #
# list = [10,25,66,78,989,'cat','tomato','right','slang', 'bizzare','absurd','towel','tulip','rotten']
# list.append('glass')
# list.append(56)
# list.append(89)
# # print(list)
# list.append(89)
# # print(list)
# list2 = ['lampooned','charles','QUEEN','consort','heiarchy']
# # list.extend(list2)
# # print(list)
# list.insert(3,'talcom powder')
# list2.insert(2,'CONGRESS')
# # print(list)
# # print(list2)
# list.extend(list2)
# print(list)
# b = list.index(78)
# print(b)
# # print(list)
# list.reverse()
# # print(list)
# a = list.index(78)
# print(a)
#
# list=[45,89,72,'xfjdj',72, 'fdcfg']
# list[1]='eighty-nine'
# print(list)
# a = list.index(72)
# print(a)

# list=[12,89,32,26,46,78,2,6,9,72,72,72]
# list.sort()
# # print(list)
# list.sort(reverse= True)
# # print(list)
# list.clear()
# print(list)
#
# a = list.count(72)
# print(a)
# b=list.index(72)
# print(b)

list = ['coconut','rockfeller','world bank','sensex', 'nifty 50', 'passive', 'income']
# print(list)
# a = list.pop(5) """ITS LIKE THE ELEMENT IN THE LIST IS REMOVED AND POPPED OUT OF THE LIST TO THE SURFACE"""
# print(a)
# # print(list)
# list.insert(5,'active')
# print(list)
# #  del function for removing
# #  remove function basically hides the a particular element
# list.__delitem__(1)
# list.remove('coconut')
# a = list.index('nifty 50')
# print(list)
# print(a)

# list=['chaitanya', 'manisha', 'tanisha', 'adrij', 'ankit']
# print(min(list))
# list.__delitem__(3)
# print(min(list))
# list.__delitem__(3)
# print(min(list))
# list.__delitem__(0)
# print(min(list))
# list.__delitem__(0)
# print(min(list))

# tup = (10,20,30,40)
# a = tup[2]
# print(a)
# tupple = (1,'HELLO', 5.32)
# print(tupple)
# t1 = (3.71)
# a = type(t1)
# print(a)
# b = type(tupple)
# print(b)
# t = tupple = (10,52,65,78)
# n = int(input("ENTER ANY NUMBER: "))
# i = 1
# while (i<=n):
#     a = input("ENTER NUMBER: ")
#     t = t + (a,)
#     i = i+1
# print("output is")
# print(t)
#
# d1 = {1:10,2:20,3:30}
# d2 = {4:40,5:50}
# d1.update(d2)
# print(d1)
# del d1[1]
# print(d1)
# a = d1.pop(3)
# print(a)
# print(d1)
# if 5 in d1:
#     print('yes')
# else: print('no')
# b = len(d1)
# print(b)
# # d1.clear()
# # print(d1)
# c = d1.keys
# print(c)
