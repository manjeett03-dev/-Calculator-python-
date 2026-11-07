#the function is done 
def calculator():
     while True:
        print("\n-----CALCULATOR-----")
        print("Enter Your Choice Of Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Exit")
        CHOICE = int(input("Enter Your Choice (1-6): "))
        if CHOICE ==1:
            print("You have selected Addition")
            A = float(input("Enter First Number: "))
            B = float(input("Enter Second Number: "))
            result = A+B
            print("The Sum of ",A,"&",B,"is: ", result)
        elif CHOICE ==2:
                print("You have selected Subtraction")
                A= float(input("Enter First Number: "))
                B= float(input("Enter Second Number: "))
                result=A-B
                print("The Difference of ",A,"&",B,"is: ", result)
        elif CHOICE ==3:
                print("You have selected Multiplication")
                A= float(input("Enter First Number: "))
                B= float(input("Enter Second Number: "))
                result= A*B
                print("The Product of ",A,"&",B,"is: ", result)
        elif CHOICE ==4:
                print("You have selected Division")
                A= float(input("Enter First Number: "))
                B= float(input("Enter Second Number: "))
                if B==0:
                   print("Error: Division by zero is not allowed.")
                else:      
                   result= A/B
                   print("The Quotient of ",A,"&",B,"is: ", result)
        elif CHOICE ==5:
                print("You have selected Power")
                A= float(input("Enter Base: "))
                B= float(input("Enter Exponent: "))
                result= A**B
                print("The Result of ",A,"^",B,"is: ", result)
        elif CHOICE == 6:
                print("You have selected Square Root")
                A= float(input("Enter Number: "))
                if A<0:
                      print("ERROR!! Square root of negative number is not defined in real numbers.")
                else:
                    result= A**0.5
                    print("The Square Root of ",A,"is: ", result)
        elif CHOICE == 7:
            print("Exiting the Calculator. Goodbye!")
            break          
        else:
            print("Invalid Choice!CHOOSE BETWEEN 1-7")
calculator()