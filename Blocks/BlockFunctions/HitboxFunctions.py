def BlockSize(x, y):
    if (x == None):
        x = 16
    if (y == None):
        y = 16
    
    # debug

    tilesX = str(x / 2)
    tilesY = str(y / 2)

    print("Tiles Used X: " + tilesX)
    print("Tiles Used Y: " + tilesY)