print("INPUT FIRST NUMBER")
num1 = int(input())
print("CHOOSE THE OPERATOR YOU WANT TO USE... "
      "1.+ "
      "2.- "
      "3.* "
      "4./ .")
operator = int(input())

print("ENTER THE SECOND NUMBER")
num2 = int(input())

if num1 == 45 and operator == 3 and num2 == 3:
    print("555")
elif num1 == 56 and operator == 1 and num2 == 9:
    print("77")
elif num1 == 56 and operator == 4 and num2 == 6:
    print("4")
elif operator == 1:
    print(int(num1)+int(num2))
elif operator == 2:
    print(int(num1)-int(num2))
elif operator == 3:
    print(int(num1)*int(num2))
elif operator == 4:
    print(int(num1)/int(num2))
