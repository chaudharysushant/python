def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y != 0:
        return x / y
    else:
        return "Invalid! Cannot divide by zero."

def calculator():
     print("Select operation:")
     print("1. Add")
     print("2. Subtract")
     print("3. Multiply")
     print("4. Divide")
     print("5. Exit")

     while True:
         choice = input ("Enter Your Choice.")
         if choice in ("1", "2", "3", "4"):
             num1 = float(input("Enter the first number:"))
             num2 = float(input("Enter the second number"))

             if choice == "1":
                 print("Result:", add(num1,num2))
                 
             if choice == "2":
                 print("Result:", subtract(num1,num2))
            
             if choice == "3":
                 print("Result:", multiply(num1,num2))
         
             if choice == "4":
                 print("Result:", divide(num1,num2))

         elif choice == "5":
             print("Exiting the calculator")
             break
         else:
             print("Invalid operation")

if __name__ == "__main__":
    calculator()