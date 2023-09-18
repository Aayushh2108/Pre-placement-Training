x = 0
y = 0
rule = int(input("enter the value of Rule: "))


# rule are given....
while(rule != 0):
    if(rule == 1):
        if(x<4):
            print("fill the x gallon jug..")
            x = 4
            print(x)
            print(y)
    elif(rule == 2):
        if(y<3):
            print("fill the y gallon jug..")
            y = 3
            print(x)
            print(y)
    elif(rule == 3):
            if(x>0):
                print("pour some water out of the x gallon jug")
                x = x - 1
                print(x)
                print(y)
    elif(rule == 4):
        if(y>0):
            print("pour some water out of the y gallon jug")
            y = y -1
            print(x)
            print(y)
    elif(rule == 5):
        if(x>0):
            print("Empty the x gallon jug..")
            x = 0
            print(x)
            print(y)
    elif(rule == 6):
        if(y>0):
            print("Empty y gallon jug..")
            y = 0
            print(x)
            print(y)
    elif(rule == 7):
        if((x+y >=4) and (y>0)):
            print("pour some water from y gallon to fill x gallon jug..")
            y = y-(4-x)
            x = 4
            print(x)
            print(y)
    elif(rule == 8):
        if((x+y>=3) and (x>0)):
            print("pour some water from y gallon jug to fill into 3 gallon jug..")
            x = x-(3-y)
            y = 3
            print(x)
            print(y)
    elif(rule == 9):
        if((x+y)<=4 and (y>0)) :
            print("pour all the water from y gallon jug into the x gallon jug..")
            x = x+y
            y = 0
            print(x)
            print(y)
    elif(rule == 10):
        if((x+y)<=3 and (x>0)):
            print("pour all the water from x gallon jug into the y gallon jug..") 
            y = x+y
            x = 0
            print(x)
            print(y)
    elif(rule == 11):
        if(x == 0 and y == 2):
            print("pour the 2 gallons from y gallon jug into x gallon jug..")
            x = 2
            y = 0
            print(x)
            print(y)
    elif(rule == 12):
        if(x == 2):
            print("empty the 2 gallon in the x gallon jug on the ground")
            x = 0
            print(x)
            print(y)
    rule  = int(input("enter the rule (0 for stop)number again: "))
