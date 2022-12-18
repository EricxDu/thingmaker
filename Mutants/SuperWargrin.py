Type = "Thing"
Name = "Super Wargrin"
Info = {
  'hit points': "300",
  'reaction time': "8",
  'pain chance': "100",
  'speed': "8",
  'width': "1310720",
  'height': "3670016",
  'mass': "500",
  'alert sound': "106",
  'action sound': "105",
  'pain sound': "27",
  'death sound': "74"
}
Frames = (
  {'sprite number':"49",'sprite subnumber': "0",'duration':"10",'action pointer':       "Look",'next frame': 1},
  {'sprite number':"49",'sprite subnumber': "1",'duration':"10",'action pointer':       "Look",'next frame': 0},
  {'sprite number':"49",'sprite subnumber': "0",'duration': "3",'action pointer':      "Chase",'next frame': 3},
  {'sprite number':"49",'sprite subnumber': "0",'duration': "3",'action pointer':      "Chase",'next frame': 4},
  {'sprite number':"49",'sprite subnumber': "1",'duration': "3",'action pointer':      "Chase",'next frame': 5},
  {'sprite number':"49",'sprite subnumber': "1",'duration': "3",'action pointer':      "Chase",'next frame': 6},
  {'sprite number':"49",'sprite subnumber': "2",'duration': "3",'action pointer':      "Chase",'next frame': 7},
  {'sprite number':"49",'sprite subnumber': "2",'duration': "3",'action pointer':      "Chase",'next frame': 8},
  {'sprite number':"49",'sprite subnumber': "3",'duration': "3",'action pointer':      "Chase",'next frame': 9},
  {'sprite number':"49",'sprite subnumber': "3",'duration': "3",'action pointer':      "Chase",'next frame': 2},
  {'sprite number':"49",'sprite subnumber': "4",'duration':"10",'action pointer': "FaceTarget",'next frame':11},
  {'sprite number':"49",'sprite subnumber': "5",'duration':"10",'action pointer': "FaceTarget",'next frame':12},
  {'sprite number':"49",'sprite subnumber': "6",'duration':"10",'action pointer':"SkelMissile",'next frame': 2},
  {'sprite number':"49",'sprite subnumber': "7",'duration': "6",'action pointer': "SkelWhoosh",'next frame':14},
  {'sprite number':"49",'sprite subnumber': "8",'duration': "6",'action pointer': "FaceTarget",'next frame':15},
  {'sprite number':"49",'sprite subnumber': "9",'duration': "6",'action pointer':    "Scratch",'next frame': 2,'unknown 1':"33",'unknown 2':"55"},
  {'sprite number':"49",'sprite subnumber':"10",'duration': "2",                               'next frame':17},
  {'sprite number':"49",'sprite subnumber':"10",'duration': "2",'action pointer':       "Pain",'next frame': 2},
  {'sprite number':"49",'sprite subnumber':"11",'duration': "8",                               'next frame':19},
  {'sprite number':"49",'sprite subnumber':"12",'duration': "8",'action pointer':     "Scream",'next frame':20},
  {'sprite number':"49",'sprite subnumber':"13",'duration': "6",                               'next frame':21},
  {'sprite number':"49",'sprite subnumber':"14",'duration': "6",'action pointer':       "Fall",'next frame':22},
  {'sprite number':"49",'sprite subnumber':"15",'duration':"-1",                                              }
)
States = {
  'initial frame': 0,
  'first moving frame': 2,
  'close attack frame': 13,
  'far attack frame': 10,
  'injury frame': 16,
  'death frame': 18
}
Flags = {
  'SOLID',
  'SHOOTABLE',
  'COUNTKILL'
}
