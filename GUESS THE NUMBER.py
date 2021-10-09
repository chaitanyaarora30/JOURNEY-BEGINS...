#lis = ["CHAITANYA", "TANISHA", "MAYANK", "SHRISHTHI"]

#for item in lis:
  #  print(item)
#list = [["CHAITANYA", 2], ["TANISHA", 3], ["MAYANK", 5], ["SHRISHTHI", 8]]
#dic1 = dict(list)


#for item, choclate in dic1.items():
 #   print(item, "and chocalte is", choclate)

#list1 = [1, 5, 8, 6, 7, 9, 88, 5, 4, 434, "harry", "chiatnya"]
#for item in list1:
 #   if str(item).isnumeric() and item>=6:
  #      print(item)

#i =0
#while(i<45) :
    #print(i)
    #i = i + 1


#i =0
#33while(True):
#    print(i +1, end=" ")
 #   if(i==44):
  #      break
   #     i = i + 1

#print("PLEASE ENTER A NUMBER")
#num = input()

#while(int(num)<100):
 #   print("TRY AGAIN")
  #  num = input()

#if(int(num))>100:
    #
#print("CONGRATULATIONS YOUR NUMBER IS GREATER THAN 100")

n = 18
print("PLEASE GUESS THE NUMBER")
print("YOU HAVE 9 CHANCES LEFT")
i = input()
if int(i) != int(n):
        print("OOPS WRONG!!.. YOU HAVE 8 CHANCE LEFT")
        input()
        while int(i) != int(n):
            print("OOPS WRONG!!.. YOU HAVE 7 CHANCE LEFT")
            input()
            while int(i) != int(n):
                print("OOPS WRONG!!.. YOU HAVE 6 CHANCE LEFT")
                input()
                while int(i) != int(n):
                    print("OOPS WRONG!!.. YOU HAVE 5 CHANCE LEFT")
                    input()
                    while int(i) != int(n):
                        print("OOPS WRONG!!.. YOU HAVE 4 CHANCE LEFT")
                        input()
                        while int(i) != int(n):
                            print("OOPS WRONG!!.. YOU HAVE 3 CHANCE LEFT")
                            input()
                            while int(i) != int(n):
                                print("OOPS WRONG!!.. YOU HAVE 2 CHANCE LEFT")
                                input()
                                while int(i) != int(n):
                                    print("OOPS WRONG!!.. YOU HAVE 1 CHANCE LEFT")
                                    input()
                                    while int(i) != int(n):
                                        print("OOPS WRONG!!.. YOU HAVE 0 CHANCE LEFT")
                                        print("DO YOU WANT TO CONTINUE?")
                                        print("PRESS y FOR YES.")
                                        print("PRESS n FOR NO.")
                                        b = input()
                                        if b == "n":
                                            break





elif int(i) == int(n):
    print("CONGRATULATIONS FOR GUESSING RIGHTLY")

