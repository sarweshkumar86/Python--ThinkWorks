# Q5. Write a Python program using match-case for numbers 1, 3, 6 and default case.
a = int(input("Enter a number between 1 and 10: "))

match a:
    case 1:
        print("You won a charger")
    case 3:
        print("You won $3")
    case 6:
        print("You won a camera")
    case _:
        print("Better luck next time")
    
