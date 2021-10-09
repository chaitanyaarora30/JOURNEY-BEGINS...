#3a = 8
#b = 8
#3#c = sum((a,b))
#print(c)

#3def function1(a,b):
 #   print("Hello you are in function 1", a+b)
#function1(8,4)

#def function2(a, b):
  #  average = (a+b)/2

   # return average

#v = function2(8,88)
#print(v)
def function2(a, b):
    """THIS FUNCTION IS A AN AVERAGE OF TWO NUMBERS
    THIS FUNCTION DOSENT WORK FOR THREE NUMBERS."""
    average = (a+b)/2
    return average

print(function2.__doc__)
print(function2(8,15))