Type = "Thing"
Name = "Enforcer"
Info = {
  'hit points': "30",
  'reaction time': "8",
  'pain chance': "170",
  'speed': "8",
  'width': "1310720",
  'height': "3670016",
  'mass': "100",
  'alert sound': "37",
  'action sound': "75",
  'pain sound': "27",
  'death sound': "60"
}
Frames = (
  {'sprite number':"30",'sprite subnumber':    "0",'duration':"10",'action pointer':      "Look",'next frame': 1},
  {'sprite number':"30",'sprite subnumber':    "1",'duration':"10",'action pointer':      "Look",'next frame': 0},
  {'sprite number':"30",'sprite subnumber':    "0",'duration': "3",'action pointer':     "Chase",'next frame': 3},
  {'sprite number':"30",'sprite subnumber':    "0",'duration': "3",'action pointer':     "Chase",'next frame': 4},
  {'sprite number':"30",'sprite subnumber':    "1",'duration': "3",'action pointer':     "Chase",'next frame': 5},
  {'sprite number':"30",'sprite subnumber':    "1",'duration': "3",'action pointer':     "Chase",'next frame': 6},
  {'sprite number':"30",'sprite subnumber':    "2",'duration': "3",'action pointer':     "Chase",'next frame': 7},
  {'sprite number':"30",'sprite subnumber':    "2",'duration': "3",'action pointer':     "Chase",'next frame': 8},
  {'sprite number':"30",'sprite subnumber':    "3",'duration': "3",'action pointer':     "Chase",'next frame': 9},
  {'sprite number':"30",'sprite subnumber':    "3",'duration': "3",'action pointer':     "Chase",'next frame': 2},
  {'sprite number':"30",'sprite subnumber':    "4",'duration':"10",'action pointer':"FaceTarget",'next frame':11},
  {'sprite number':"30",'sprite subnumber':"32773",'duration':"10",'action pointer':"SPosAttack",'next frame':12},
  {'sprite number':"30",'sprite subnumber':    "4",'duration':"10",                              'next frame': 2},
  {'sprite number':"30",'sprite subnumber':    "6",'duration': "3",                              'next frame':14},
  {'sprite number':"30",'sprite subnumber':    "6",'duration': "3",'action pointer':      "Pain",'next frame': 2},
  {'sprite number':"30",'sprite subnumber':    "7",'duration': "5",                              'next frame':16},
  {'sprite number':"30",'sprite subnumber':    "8",'duration': "5",'action pointer':    "Scream",'next frame':17},
  {'sprite number':"30",'sprite subnumber':    "9",'duration': "5",'action pointer':      "Fall",'next frame':18},
  {'sprite number':"30",'sprite subnumber':   "10",'duration': "5",                              'next frame':19},
  {'sprite number':"30",'sprite subnumber':   "11",'duration': "5",                              'next frame':20},
  {'sprite number':"30",'sprite subnumber':   "12",'duration':"-1",                            'next frame':None},
)
States = {
  'initial frame': 0,
  'first moving frame': 2,
  'far attack frame': 10,
  'injury frame': 13,
  'death frame': 15
}
Flags = {
  'SOLID',
  'SHOOTABLE',
  'COUNTKILL'
}
