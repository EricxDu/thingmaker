Type = "Weapon"
Name = "Super Chaingun"
Info = {
  'ammo type': "0",  #bullets
}
Frames = (
  {'sprite number':"7",'sprite subnumber':    "0",'duration':"1",'action pointer':"WeaponReady",'next frame': 0 },
  {'sprite number':"7",'sprite subnumber':    "0",'duration':"1",'action pointer':      "Lower",'next frame': 1 },
  {'sprite number':"7",'sprite subnumber':    "0",'duration':"1",'action pointer':      "Raise",'next frame': 2 },
  {'sprite number':"7",'sprite subnumber':    "0",'duration':"2",'action pointer':   "FireCGun",'next frame': 4 },  #52
  {'sprite number':"7",'sprite subnumber':    "1",'duration':"2",'action pointer':   "FireCGun",'next frame': 5 },  #53
  {'sprite number':"7",'sprite subnumber':    "1",'duration':"0",'action pointer':     "ReFire",'next frame': 6 },  #54
  {'sprite number':"7",'sprite subnumber':    "0",'duration':"3",'action pointer':     "Refire",'next frame': 7 },  #996
  {'sprite number':"7",'sprite subnumber':    "1",'duration':"3",'action pointer':     "Refire",'next frame': 8 },  #997
  {'sprite number':"7",'sprite subnumber':    "0",'duration':"6",'action pointer':     "Refire",'next frame': 9 },  #777
  {'sprite number':"7",'sprite subnumber':    "1",'duration':"6",'action pointer':     "Refire",'next frame': 0 },  #998
  {'sprite number':"8",'sprite subnumber':"32768",'duration':"5",'action pointer':     "Light1",'next frame':"1"},
  {'sprite number':"8",'sprite subnumber':"32769",'duration':"5",'action pointer':     "Light2",'next frame':"1"},
)
States = {
  'bobbing frame': 0,
  'select frame': 1,
  'deselect frame': 2,
  'shooting frame': 3,
  'firing frame': 10
}
