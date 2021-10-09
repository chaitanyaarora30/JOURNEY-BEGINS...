print("ENTER NUMBER 1")
num1 = input()
print("ENTER NUMBER 2")
num2 = input()

try:
    print("the sum of these two numbers is",
          int(num1) + int(num2))
except Exception as e:
    print(e)
print("This line is very important")