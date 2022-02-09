# This is to try and implement a recursive factorial algorithm

def find_factorial(n):
  if n ==1:
    return n
  else:
    return (n*find_factorial(n-1))

while(True):
  user_int = int(input("Enter a number you would like to find the factorial of:\t"))
  print("The factorial of " + str(user_int) + " is " + str(find_factorial(user_int)))