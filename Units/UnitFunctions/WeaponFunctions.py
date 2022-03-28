def WeaponCenter(x, y):
    if (x == None):
        x = 4
    if (y == None):
        y = 4
    
    # debug

    x = str(x)
    y = str(y)

    print("Weapon Center: " + x + ", " + y)

def BulletSpawnSide(side):
    if (side == None):
        side = "Front"
    
    # debug

    print("Bullet Spawn Side: " + side)

def WeaponRotateLimits(leftLimit, rightLimit):
    if (leftLimit == None):
        leftLimit = 0
    if (rightLimit == None):
        rightLimit = 0
    
    # debug

    leftLimit = str(leftLimit)
    rightLimit = str(rightLimit)

    print("Left Rotation Limit: " + leftLimit)
    print("Right Rotation Limit: " + rightLimit)

def WeaponRotatePoint(rotateX, rotateY):
    if (rotateX == None):
        rotateX = x
    if (rotateY == None):
        rotateY = y
    
    # debug

    rotateX = str(rotateX)
    rotateY = str(rotateY)

    print("Rotation Point: " + rotateX + ", " + rotateY)

def WeaponTarget(type1, type2, type3):
    if (type1 == None):
        type1 = "Opposing_Core"
    if (type2 == None):
        type2 = "Opposing_Units"
    if (type3 == None):
        type3 = "Opposing_Blocks"
    
    # debug

    print("Weapon Primary Target Type: " + type1)
    print("Weapon Secondary Target Type: " + type2)
    print("Weapon Tertiary Target Type: " + type3)

def WeaponAmmoType(ammo):
    if (ammo == None):
        ammo = "short_ranged"
    
    # debug

    print("Weapon Ammo Type" + ammo)

def WeaponParent(name):
    if (name == None):
        name = "MainBody"
    
    # debug

    print("Weapon Parent: " + name)