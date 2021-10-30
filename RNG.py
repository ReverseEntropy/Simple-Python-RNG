import random as r
try:
    minNum = int(input("Enter min: \n"))
    maxNum = int(input("Enter max: \n"))
    inputnums = int(input("How many numbers do you want to generate?\n"))
    print("\n")
    print("==============================================")
    if inputnums == 1:
        rand = r.randint(minNum, maxNum)
        print("==============================================")
        print(rand)
    else:
        for x in range(inputnums):
            y = r.randint(minNum,maxNum)
            print(y)
    print("==============================================")
except ValueError:
    print("ERROR: You entered an incorrect value for min/max")



