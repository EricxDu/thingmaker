Type = "Thing"
Name = "Hindring"
Info = {
  'hit points': 150,
  'reaction time': 8,
  'pain chance': 180,
  'speed': 10,
  'width': 1966080,
  'height': 3670016,
  'mass': 400,
  'alert sound': 41,
  'attack sound': 52,
  'action sound': 77,
  'pain sound': 26,
  'death sound': 64
}
Frames = (
  {'sprite number':39, 'sprite subnumber':0, 'duration':10, 'action pointer':"Look",      'next frame':1 },
  {'sprite number':39, 'sprite subnumber':1, 'duration':10, 'action pointer':"Look",      'next frame':0 },
  {'sprite number':39, 'sprite subnumber':0, 'duration':2, 'action pointer':"Chase",      'next frame':3 },
  {'sprite number':39, 'sprite subnumber':0, 'duration':2, 'action pointer':"Chase",      'next frame':4 },
  {'sprite number':39, 'sprite subnumber':1, 'duration':2, 'action pointer':"Chase",      'next frame':5 },
  {'sprite number':39, 'sprite subnumber':1, 'duration':2, 'action pointer':"Chase",      'next frame':6 },
  {'sprite number':39, 'sprite subnumber':2, 'duration':2, 'action pointer':"Chase",      'next frame':7 },
  {'sprite number':39, 'sprite subnumber':2, 'duration':2, 'action pointer':"Chase",      'next frame':8 },
  {'sprite number':39, 'sprite subnumber':3, 'duration':2, 'action pointer':"Chase",      'next frame':9 },
  {'sprite number':39, 'sprite subnumber':3, 'duration':2, 'action pointer':"Chase",      'next frame':2 },
  {'sprite number':39, 'sprite subnumber':4, 'duration':8, 'action pointer':"FaceTarget", 'next frame':11},
  {'sprite number':39, 'sprite subnumber':5, 'duration':8, 'action pointer':"FaceTarget", 'next frame':12},
  {'sprite number':39, 'sprite subnumber':6, 'duration':8, 'action pointer':'SargAttack', 'next frame':2 },
  {'sprite number':39, 'sprite subnumber':7, 'duration':2,                                'next frame':14},
  {'sprite number':39, 'sprite subnumber':7, 'duration':2, 'action pointer':"Pain",       'next frame':2 },
  {'sprite number':39, 'sprite subnumber':8, 'duration':8,                                'next frame':16},
  {'sprite number':39, 'sprite subnumber':9, 'duration':8, 'action pointer':"Scream",     'next frame':17},
  {'sprite number':39, 'sprite subnumber':10, 'duration':4,                               'next frame':18},
  {'sprite number':39, 'sprite subnumber':11, 'duration':4, 'action pointer':"Fall",      'next frame':19},
  {'sprite number':39, 'sprite subnumber':12, 'duration':4,                               'next frame':20},
  {'sprite number':39, 'sprite subnumber':13, 'duration':-1,                            'next frame':None}
)
States = {
  'initial frame': 0,
  'first moving frame': 2,
  'close attack frame': 10,
  'injury frame': 13,
  'death frame': 15
}
Flags = {
  'SOLID',
  'SHOOTABLE',
  'COUNTKILL'
}
