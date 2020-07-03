# CP3-Sirisat-Waeowannajit
print("----------------------------------------\n>Login<\n")
a= input("Username: ")
b= int(input("Password: "))

if a == "Sirisat" and b == 1234:
    print("\n----------------------------------------\n\n\n\n            Welcome To iFruit!")
    print("          ======================")
    print("               >Fruit List<")
    print("          Banana     x1  5(THB)")
    print("          Mango      x1 10(THB)")
    print("          Papaya     x1 10(THB)")
    input("\n<Continue?>")
    print("\n\n\n----------------------------------------")
    print("\nRobot: How can I help you customer?")
    x = int(input("\n You : 1)  I want banana. \n       2)  I want mango. \n       3)  I want papaya.\n\nYour Choice: "))
    if x == 1:
        print("\n----------------------------------------")
        print("\nRobot: How many Banana?")
        z= int(input("\n You : "))
        result= z * 5
        print("\nRobot: Total price is",result)
        print("\n You : Thanks!")
        print("\nRobot: Your Welcome!")
        print("\n----------------------------------------")
    elif x == 2:
        print("\n----------------------------------------")
        print("\nRobot: How many Mango?")
        z = int(input("\n You : "))
        result = z * 10
        print("\nRobot: Total price is",result)
        print("\n You : Thanks!")
        print("\nRobot: Your Welcome!")
        print("\n----------------------------------------")
    else:
        print("\n----------------------------------------")
        print("\nRobot: How many Papaya?")
        z = int(input("\n You : "))
        result = z * 10
        print("\nRobot: Total price is",result)
        print("\n You : Thanks!")
        print("\nRobot: Your Welcome!")
        print("\n----------------------------------------")
else:
    print("Incorrect Username or Password.")
