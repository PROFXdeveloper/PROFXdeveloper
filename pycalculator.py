print(" Select an operation to perform")
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")

operation = input()

if operation == "A":
    a,b = input("Addition: ").split(" and ")
    print("Answer: " + str(int(a) + int(b)))

elif operation == "B":
    a,b = input("Subtraction: ").split(" and ")
    print("Answer: " + str(int(a) - int(b)))

elif operation == "C":
    a,b = input("Multiplication: ").split(" and ")
    print("Answer: " + str(int(a) * int(b)))
    
elif operation == "D":
    a,b = input("Division: ").split(" and ")
    print("Answer: " + str(int(a) / int(b)))
    
elif operation == "a":
    print("invalid operation")

elif operation == "b":
    print("invalid operation")

elif operation == "c":
    print("invalid operation")

elif operation == "d":
    print("invalid operation")
