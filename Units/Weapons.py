import UnitFunctions.WeaponFunctions
import UnitFunctions.TextureFunctions

Weapons = UnitFunctions.WeaponFunctions
Textures = UnitFunctions.TextureFunctions
Tier1LeftX = 0
Tier1LeftY = 0
Tier1RightX = 0
Tier1RightY = 0
Tier1CenterX = 0

def Tier1WeaponOffenceLeft(Tier1LeftX, Tier1LeftY):
    Weapons.WeaponCenter(Tier1LeftX, Tier1LeftY)
    Weapons.WeaponRotateLimits(45, 0)
    Weapons.WeaponRotatePoint(Tier1LeftX-2, Tier1LeftY-1)
    Weapons.WeaponAmmoType("short_ranged")
    Weapons.BulletSpawnSide("front")
    Weapons.WeaponTarget("Opposing_Core", "Opposing_Units", "Opposing_Blocks")
    Weapons.WeaponParent("MainBody")
    Textures.WeaponTextureName("assets.units.weapons.Tier1WeaponOffenceLeft.png")

def Tier1WeaponOffenceRight(Tier1RightX, Tier1RightY):
    Weapons.WeaponCenter(Tier1RightX, Tier1RightY)
    Weapons.WeaponRotateLimits(0, 45)
    Weapons.WeaponRotatePoint(Tier1RightX-2, Tier1RightY-1)
    Weapons.WeaponAmmoType("short_ranged")
    Weapons.BulletSpawnSide("front")
    Weapons.WeaponTarget("Opposing_Core", "Opposing_Units", "Opposing_Blocks")
    Weapons.WeaponParent("MainBody")
    Textures.WeaponTextureName("assets.units.weapons.Tier1WeaponOffenceRight.png")

def Tier1WeaponSuicide():
    Weapons.WeaponAmmoType("bomb")
    Weapons.WeaponTarget("Opposing_Code", "Opposing_Units", "Opposing_Blocks")
    Weapons.WeaponParent("MainBody")

def Tier1WeaponOffenceCenterSlither(Tier1CenterX):
    Weapons.BulletSpawnSide("back")
    Weapons.WeaponAmmoType("short_range")
    Weapons.WeaponCenter(-4, 0)
    Weapons.WeaponParent("tailFour")
    Weapons.WeaponRotateLimits(45, 45)
    Weapons.WeaponRotatePoint(-4, 0)
    Weapons.WeaponTarget("Opposing_Core", "Opposing_Units", "Opposing_Blocks")
    Textures.WeaponTextureName("assets.units.weapons.SlitherTier1TailWeapon.png")