"""
A brackets problem.
If user enters number 3, output should be - 
() () ()
(()) ()
() (())
((()))
If user enters number 4, output should be -
() () () ()
(()) () ()
() (()) ()
() () (())
((())) ()
() ((()))
(((())))
"""


def bracketise(n):
    left = "("
    right = ")"
    for i in range(n):
        for j in range(i):
            print(left, end="")
        for j in range(i):
            print(right, end="")
        for j in range(i):
          print(left + right, end="")

        print(" ")



while True:
    userInput = int(input("Enter a number: "))
    bracketise(userInput)
