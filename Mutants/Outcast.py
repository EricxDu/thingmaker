Type = "Thing"
Name = "Outleader"
Info = {
  'hit points': "500",
  'reaction time': "8",
  'pain chance': "50",
  'speed': "8",
  'width': "1572864",
  'height': "4194304",
  'mass': "1000",
  'alert sound': "43",
  'action sound': "77",
  'pain sound': "26",
  'death sound': "67"
}
Frames = (
  {'sprite number':"43",'sprite subnumber': "0",'duration':"10",'action pointer':"Look",       'next frame': 1},
  {'sprite number':"43",'sprite subnumber': "1",'duration':"10",'action pointer':"Look",       'next frame': 0},
  {'sprite number':"43",'sprite subnumber': "0",'duration': "3",'action pointer':"Chase",      'next frame': 3},
  {'sprite number':"43",'sprite subnumber': "0",'duration': "3",'action pointer':"Chase",      'next frame': 4},
  {'sprite number':"43",'sprite subnumber': "1",'duration': "3",'action pointer':"Chase",      'next frame': 5},
  {'sprite number':"43",'sprite subnumber': "1",'duration': "3",'action pointer':"Chase",      'next frame': 6},
  {'sprite number':"43",'sprite subnumber': "2",'duration': "3",'action pointer':"Chase",      'next frame': 7},
  {'sprite number':"43",'sprite subnumber': "2",'duration': "3",'action pointer':"Chase",      'next frame': 8},
  {'sprite number':"43",'sprite subnumber': "3",'duration': "3",'action pointer':"Chase",      'next frame': 9},
  {'sprite number':"43",'sprite subnumber': "3",'duration': "3",'action pointer':"Chase",      'next frame': 2},
  {'sprite number':"43",'sprite subnumber': "4",'duration': "8",'action pointer':"FaceTarget", 'next frame':11},
  {'sprite number':"43",'sprite subnumber': "5",'duration': "8",'action pointer':"FaceTarget", 'next frame':12},
  {'sprite number':"43",'sprite subnumber': "6",'duration': "8",'action pointer':'BruisAttack','next frame': 2},
  {'sprite number':"43",'sprite subnumber': "7",'duration': "0",'action pointer':"FaceTarget", 'next frame':14},
  {'sprite number':"43",'sprite subnumber': "7",'duration': "6",'action pointer':'SkelWhoosh', 'next frame':15},
  {'sprite number':"43",'sprite subnumber': "8",'duration': "6",'action pointer':"FaceTarget", 'next frame':16},
  {'sprite number':"43",'sprite subnumber': "9",'duration': "6",'action pointer':'SkelFist',   'next frame': 2},
  {'sprite number':"43",'sprite subnumber':"10",'duration': "2",                               'next frame':18},
  {'sprite number':"43",'sprite subnumber':"10",'duration': "2",'action pointer':"Pain",       'next frame': 2},
  {'sprite number':"43",'sprite subnumber':"11",'duration': "8",                               'next frame':20},
  {'sprite number':"43",'sprite subnumber':"12",'duration': "8",'action pointer':"Scream",     'next frame':21},
  {'sprite number':"43",'sprite subnumber':"13",'duration': "8",                               'next frame':22},
  {'sprite number':"43",'sprite subnumber':"14",'duration': "8",'action pointer':"Fall",       'next frame':23},
  {'sprite number':"43",'sprite subnumber':"15",'duration': "8",                               'next frame':24},
  {'sprite number':"43",'sprite subnumber':"16",'duration':"-1",                                              }
)
States = {
  'initial frame': 0,
  'first moving frame': 2,
  'close attack frame': 13,
  'far attack frame': 10,
  'injury frame': 17,
  'death frame': 19
}
Flags = {
  'SOLID',
  'SHOOTABLE',
  'COUNTKILL'
}
