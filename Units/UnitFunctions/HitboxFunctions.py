EntityShapeRadius1 = 0
EntityShapeRadius2 = 0
BlockShapeRadius1 = 0
BlockShapeRadius2 = 0

def EntityHitboxSize(xRadius, yRadius):
    if (xRadius == None):
        xRadius = 8
    
    if (yRadius == None):
        yRadius = 8
    
    xRadius = abs(xRadius)
    yRadius = abs(yRadius)
    EntityShapeRadius1 = xRadius
    EntityShapeRadius2 = yRadius

    # debug

    xRadius = str(xRadius)
    yRadius = str(yRadius)

    print("Entity Hitbox X Radius: " + xRadius)
    print("Entity Hitbox Y Radius: " + yRadius)

def EntityHitboxShape(shape):
    if (shape == None):
        shape = "square"
    
    shape = shape.lower()

    # debug

    print("Entity Hitbox Shape: " + shape)

def HitboxCenter(x, y):
    if (x == None):
        x = 0
    
    if (y == None):
        y = 0
    
    # debug

    x = str(x)
    y = str(y)

    print("Hitbox Center Point:" + x + ", " + y)

def BlockHitboxSize(xRadius, yRadius):
    if (xRadius == None):
        xRadius = 8
    
    if (yRadius == None):
        yRadius = 8
    
    BlockShapeRadius1 = xRadius
    BlockShapeRadius2 = yRadius

    # debug

    xRadius = str(xRadius)
    yRadius = str(yRadius)

    print("Block Hitbox X Radius: " + xRadius)
    print("Block Hitbox Y Radius: " + yRadius)

def BlockHitboxShape(shape):
    if (shape == None):
        shape = "square"
    
    shape = shape.lower()

    # debug

    print("Block Hitbox Shape: " + shape)