Type = "Thing"
Name = "Green Fireball"
Info = {
  'hit points': 1000,
  'reaction time': 8,
  'pain chance': 0,
  'speed': 983040,
  'width': 393216,
  'height': 524288,
  'mass': 100,
  'alert sound': 16,
}
Frames = (
  {'sprite number':41,'sprite subnumber':32768,'duration':4,'next frame': 1},
  {'sprite number':41,'sprite subnumber':32769,'duration':4,'next frame': 0},
  {'sprite number':41,'sprite subnumber':32770,'duration':6,'next frame': 3},
  {'sprite number':41,'sprite subnumber':32771,'duration':6,'next frame': 4},
  {'sprite number':41,'sprite subnumber':32772,'duration':6,'next frame':""}
)
States = {
  'initial frame': 0,
  'death frame': 2
}
Flags = {
  'NOBLOCKMAP',
  'MISSILE',
  'DROPOFF',
  'NOGRAVITY'
}
