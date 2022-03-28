import UnitFunctions.HealthFunctions
import UnitFunctions.HitboxFunctions
import UnitFunctions.MovementFunctions
import UnitFunctions.TextureFunctions
import Weapons

Health = UnitFunctions.HealthFunctions
Hitbox = UnitFunctions.HitboxFunctions
Movement = UnitFunctions.MovementFunctions
Texture = UnitFunctions.TextureFunctions

class PlayerTier1:
    Health.HealthValue(20)
    Hitbox.EntityHitboxSize(8, 8)
    Hitbox.EntityHitboxShape("circle")
    Hitbox.BlockHitboxSize(8, 8)
    Hitbox.BlockHitboxShape("square")
    Hitbox.HitboxCenter(0, 0)
    Movement.MovementFly()
    Texture.TextureName("assets.units.PlayerTier1.png")
    print(">> Left Weapon")
    Weapons.Tier1WeaponOffenceLeft(4, 4)
    print(">> Right Weapon")
    Weapons.Tier1WeaponOffenceRight(-4, 4)