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
        print(left+right, end="")

    print(" ")



    for i in range(n):
        print(left, end="")
    for i in range(n):
        print(right, end="")
    
    print(" ")



while True:
    userInput = int(input("Enter a number: "))
    bracketise(userInput)
