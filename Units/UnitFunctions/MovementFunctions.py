def MovementFly():

    # debug

    print("Movement Mode: Fly")

def MovementBipedal():

    # debug

    print("Movement Mode: Walk")

def LegDistanceFromCenter(x, y):
    if (x == None):
        x = 0
    if (y == None):
        y = 0
    
    # debug

    y = str(y)
    x = str(x)

    print("Leg Distance From Center: " + x + ", " + y)

def MovementMultipedal():

    # debug

    print("Movement Mode: Crawl")

def LegLength(upperDis, kneeDis, lowerDis):
    if (upperDis == None):
        upperDis = 4
    if (kneeDis == None):
        kneeDis = 2
    if (lowerDis == None):
        lowerDis = 4
    
    # debug

    upperDis = str(upperDis)
    kneeDis = str(kneeDis)
    lowerDis = str(lowerDis)

    print("Upper Leg Length: " + upperDis)
    print("Knee Distance Length: " + kneeDis)
    print("Lower Leg Distane: " + lowerDis)

def LegCount(legNum):
    if (legNum == None):
        legNum = 4
    
    # debug

    legNum = str(legNum)

    print("Leg Count: " + legNum)

def MovementSlither():

    # debug

    print("Movement Mode: Slither")

def UnitTargetType(Type1, Type2, Type3):
    if (Type1 == None):
        Type1 = "Core"
    if (Type2 == None):
        Type2 = "Opposing Units"
    if (Type3 == None):
        Type3 == "Opposing Blocks"
    
    # debug

    print("Primary Target Type: " + Type1)
    print("Secondary Target Type: " + Type2)
    print("Teritary Target Type: " + Type3)