import UnitFunctions.HealthFunctions
import UnitFunctions.HitboxFunctions
import UnitFunctions.MovementFunctions
import UnitFunctions.TextureFunctions
import Weapons

Health = UnitFunctions.HealthFunctions
Hitbox = UnitFunctions.HitboxFunctions
Movement = UnitFunctions.MovementFunctions
Textures = UnitFunctions.TextureFunctions

class FlyingUnitTier1:
    Health.HealthValue(20)
    Hitbox.HitboxCenter(0, 0)
    Hitbox.EntityHitboxSize(8, 8)
    Hitbox.EntityHitboxShape("circle")
    Hitbox.BlockHitboxSize(8, 8)
    Hitbox.BlockHitboxShape("square")
    Movement.MovementFly()
    Movement.UnitTargetType("Opposing_Core", "Opposing_Units", "Opposing_Blocks")
    Movement.LegDistanceFromCenter(4, -2)
    Textures.TextureName("assets.units.FlyingTier1.png")
    Textures.FlyWingTextureLeft("assets.units.FlyingTier1WingLeft.png")
    Textures.FlyWingTextureRight("assets.units.FlyingTier1WingRight.png")
    print(">> Left Weapon")
    Weapons.Tier1WeaponOffenceLeft(4, 6)
    print(">> Right Weapon")
    Weapons.Tier1WeaponOffenceRight(-4, 6)

class WalkingUnitTier1:
    Health.HealthValue(20)
    Hitbox.EntityHitboxSize(8, 8)
    Hitbox.EntityHitboxShape("circle")
    Hitbox.BlockHitboxSize(8, 8)
    Hitbox.BlockHitboxShape("square")
    Hitbox.HitboxCenter(0, 0)
    Movement.MovementBipedal()
    Movement.LegDistanceFromCenter(4, 0)
    Movement.UnitTargetType("Opposing_Core", "Opposing_Units", "Opposing_Blocks")
    Textures.TextureName("assets.units.WalkingTier1.png")
    Textures.BipedalLegTextureLeft("assets.units.WalkingTier1LeftLeg.png")
    Textures.BipedalLegTextureRight("assets.units.WalkingTier1RightLeg.png")
    print(">> Left Weapon")
    Weapons.Tier1WeaponOffenceLeft(4, 0)
    print(">> Right Weapon")
    Weapons.Tier1WeaponOffenceRight(-4, 0)

class CrawlingUnitTier1:
    Health.HealthValue(20)
    Hitbox.EntityHitboxSize(8, 8)
    Hitbox.EntityHitboxShape("circle")
    Hitbox.BlockHitboxSize(8, 8)
    Hitbox.BlockHitboxShape("square")
    Hitbox.HitboxCenter(0, 0)
    Movement.MovementMultipedal()
    Movement.LegCount(4)
    Movement.LegLength(4, 2, 4)
    Textures.TextureName("assets.units.CrawlingUnitTier1.png")
    Textures.MultipedalUpperLegTexture("assets.units.CrawlingUnitTier1UpperLeg.png")
    Textures.MultipedalKneeLegTexture("assets.units.CrawlingUnitTier1Knee.png")
    Textures.MultipedalLowerLegTexture("assets.units.CrawlingUnitTier1LowerLeg.png")
    Textures.MultipedalFootLegTexture("assets.units.CrawlingUnitTier1Foot.png")
    print(">> Weapon")
    Weapons.Tier1WeaponSuicide()

