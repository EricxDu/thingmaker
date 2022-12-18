Type = "Thing"
Name = "Droid"
Info = {
  'hit points': "500",
  'reaction time': "8",
  'pain chance': "128",
  'speed': "12",
  'width': "1310720",
  'height': "3670016",
  'mass': "600",
  'alert sound': "46",
  'action sound': "78",
  'pain sound': "103",  #26
  'death sound': "104"  #70
}
Frames = (
  {'sprite number':"46", 'sprite subnumber':"0", 'duration':"10", 'action pointer':"Look",       'next frame': 1},
  {'sprite number':"46", 'sprite subnumber':"1", 'duration':"10", 'action pointer':"Look",       'next frame': 0},
  {'sprite number':"46", 'sprite subnumber':"0", 'duration':"3", 'action pointer':"Chase",       'next frame': 3},
  {'sprite number':"46", 'sprite subnumber':"0", 'duration':"3", 'action pointer':"Chase",       'next frame': 4},
  {'sprite number':"46", 'sprite subnumber':"1", 'duration':"3", 'action pointer':"Chase",       'next frame': 5},
  {'sprite number':"46", 'sprite subnumber':"1", 'duration':"3", 'action pointer':"Chase",       'next frame': 6},
  {'sprite number':"46", 'sprite subnumber':"2", 'duration':"3", 'action pointer':"Chase",       'next frame': 7},
  {'sprite number':"46", 'sprite subnumber':"2", 'duration':"3", 'action pointer':"Chase",       'next frame': 8},
  {'sprite number':"46", 'sprite subnumber':"3", 'duration':"3", 'action pointer':"Chase",       'next frame': 9},
  {'sprite number':"46", 'sprite subnumber':"3", 'duration':"3", 'action pointer':"Chase",       'next frame': 2},
  {'sprite number':"46", 'sprite subnumber':"4", 'duration':"10", 'action pointer':"FaceTarget", 'next frame':11},
  {'sprite number':"46", 'sprite subnumber':"5", 'duration':"4", 'action pointer':'CPosAttack',  'next frame':12},
  {'sprite number':"46", 'sprite subnumber':"6", 'duration':"4", 'action pointer':'CPosAttack',  'next frame':13},
  {'sprite number':"46", 'sprite subnumber':"4", 'duration':"1", 'action pointer':'CPosRefire',  'next frame':11},
  {'sprite number':"46", 'sprite subnumber':"7", 'duration':"3",                                 'next frame':15},
  {'sprite number':"46", 'sprite subnumber':"7", 'duration':"3", 'action pointer':"Pain",        'next frame': 2},
  {'sprite number':"46", 'sprite subnumber':"8", 'duration':"5",                                 'next frame':17},
  {'sprite number':"46", 'sprite subnumber':"9", 'duration':"5", 'action pointer':"Scream",      'next frame':18},
  {'sprite number':"46", 'sprite subnumber':"10", 'duration':"5",                                'next frame':19},
  {'sprite number':"46", 'sprite subnumber':"11", 'duration':"5",                                'next frame':20},
  {'sprite number':"46", 'sprite subnumber':"12", 'duration':"5",                                'next frame':21},
  {'sprite number':"46", 'sprite subnumber':"13", 'duration':"5", 'action pointer':"Fall",       'next frame':22},
  {'sprite number':"46", 'sprite subnumber':"14", 'duration':"-1",                               'next frame':""},
)
States = {
  'initial frame': 0,
  'first moving frame': 2,
  'far attack frame': 10,
  'injury frame': 14,
  'death frame': 16
}
Flags = {
  'SOLID',
  'SHOOTABLE',
  'FLOAT',
  'NOGRAVITY',
  'COUNTKILL'
}
