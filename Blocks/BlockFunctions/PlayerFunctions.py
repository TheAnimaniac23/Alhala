def PlayerSpawnType(typeClass):
    if (typeClass == None):
        typeClass = "PlayerTier1"
    
    # debug

    print("Spawn Player Type: " + typeClass)

def PlayerRespawnTime(time):
    if (time == None):
        time = 10
    
    # debug

    time = str(time)

    print("Player Respawn Time: " + time)

def PlayerRespawnCostResources(boolean):
    if (boolean == None):
        boolean = True