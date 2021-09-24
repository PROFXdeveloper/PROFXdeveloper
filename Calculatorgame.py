def new_game():
    print("ADD")
    num1=int(input("Num1: "))
    num2=int(input("Num2: "))

    print(num1+num2)


    print("SUB")
    num1=int(input("Num1: "))
    num2=int(input("Num2: "))

    print(num1-num2)

    print("MUL")
    num1=int(input("Num1: "))
    num2=int(input("Num2: "))

    print(num1*num2)


def play_again():

    print("Do you want to play  again? ")
    re=input("yes or no ")

    if re == "yes":
        return True
    else:
        return False
              

new_game()
    

while play_again():
    new_game()

print("Goodbye!! ")
