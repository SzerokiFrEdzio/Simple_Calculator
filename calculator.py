#Create the functions
def Addition(x, y):
    return x + y

def Substraction(x, y):
    return x - y


def Multiplication(x, y):
    return x * y


def Division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'nie dziel przez zero'

#create welcoming page
print("Hello, lets do some math! ")
print("Choose what are we doing:")
print(" 1. Addition 2. Substraction 3. Multiplication 4. Division ")
#return point
while True:
    choice = input()
    if choice in ('1', '2', '3', '4'): 
#def. numbers
        
            num1 = float(input("Enter your first number: "))
            num2 = float(input('Enter your second number: '))
#create commands  
        
            if choice == '1':
                print(num1, "+", num2, "=", Addition(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", Substraction(num1, num2))
            elif choice == '3':
                print(num1, "x", num2, "=", Multiplication(num1, num2))
            elif choice == '4':
                print(num1, '/', num2, '=', Division(num1, num2))
       
            next= input("One more time? yes/no ")
            if next == "yes":
                print('Please choose: ')
            if next == "no":
                print("See ya next time! ")
            break  
    else:
        print("I'm counting only on numbers and on you. Try again")
        