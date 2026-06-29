score = int(input("Enter your score: "))
oneDigit = score // 10

match oneDigit :
    case 10 | 9 :
        print("Excellent!")
    case 8 :
        print("Good job!") 
    case 7 :
        print("you can do better.")
    case 6 :
        print("you need to work harder.")
    case _ :
        print("you need to improve you performance.")

print("Thank you for using the grade evaluator.")