Type = "Weapon"
Name = "Super Pistol"
Info = {
  'ammo type': "0",  #bullets
}
Frames = (
  {'sprite number':"3",'sprite subnumber':    "0",'duration':"1",'action pointer':"WeaponReady",'next frame': 0 },
  {'sprite number':"3",'sprite subnumber':    "0",'duration':"1",'action pointer':      "Lower",'next frame': 1 },
  {'sprite number':"3",'sprite subnumber':    "0",'duration':"1",'action pointer':      "Raise",'next frame': 2 },
  {'sprite number':"3",'sprite subnumber':    "2",'duration':"3",'action pointer':       "Null",'next frame': 4 },  #13
  {'sprite number':"3",'sprite subnumber':"32771",'duration':"3",'action pointer': "FirePistol",'next frame': 5 },  #14
  {'sprite number':"3",'sprite subnumber':    "4",'duration':"3",'action pointer':       "Null",'next frame': 6 },  #15
  {'sprite number':"3",'sprite subnumber':"32769",'duration':"2",'action pointer':     "ReFire",'next frame': 0 },  #16
  {'sprite number':"4",'sprite subnumber':"32768",'duration':"3",'action pointer':     "Light1",'next frame':"1"},  #17
)
States = {
  'bobbing frame': 0,
  'select frame': 1,
  'deselect frame': 2,
  'shooting frame': 3,
  'firing frame': 7
}
