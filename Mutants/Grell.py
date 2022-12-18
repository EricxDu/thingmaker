Type = "Thing"
Name = "Grell"
Info = {
  'hit points': 100,
  'pain chance': 256,
  'speed': 8,
  'width': 1048576,
  'height': 3670016,
  'mass': 50,
  'damage': 3,
  'attack sound': 51,
  'action sound': 77,
  'death sound': 17
}
Frames = (
  {'sprite number':50, 'sprite subnumber':0,  'duration':10, 'action pointer':"Look",       'next frame':0 },
  {'sprite number':50, 'sprite subnumber':0,  'duration':3,  'action pointer':"Chase",      'next frame':2 },
  {'sprite number':50, 'sprite subnumber':0,  'duration':3,  'action pointer':"Chase",      'next frame':3 },
  {'sprite number':50, 'sprite subnumber':1,  'duration':3,  'action pointer':"Chase",      'next frame':4 },
  {'sprite number':50, 'sprite subnumber':1,  'duration':3,  'action pointer':"Chase",      'next frame':5 },
  {'sprite number':50, 'sprite subnumber':2,  'duration':3,  'action pointer':"Chase",      'next frame':6 },
  {'sprite number':50, 'sprite subnumber':2,  'duration':3,  'action pointer':"Chase",      'next frame':1 },
  {'sprite number':50, 'sprite subnumber':3,  'duration':10, 'action pointer':"FaceTarget", 'next frame':8 },
  {'sprite number':50, 'sprite subnumber':4,  'duration':4,  'action pointer':'SkullAttack','next frame':9 },
  {'sprite number':50, 'sprite subnumber':5,  'duration':4,                                 'next frame':9 },
  {'sprite number':50, 'sprite subnumber':6,  'duration':3,                                 'next frame':11},
  {'sprite number':50, 'sprite subnumber':6,  'duration':3,  'action pointer':"Pain",       'next frame':1 },
  {'sprite number':50, 'sprite subnumber':7,  'duration':6,                                 'next frame':13},
  {'sprite number':50, 'sprite subnumber':8,  'duration':6,  'action pointer':"Scream",     'next frame':14},
  {'sprite number':50, 'sprite subnumber':9,  'duration':6,                                 'next frame':15},
  {'sprite number':50, 'sprite subnumber':10, 'duration':6,                                 'next frame':16},
  {'sprite number':50, 'sprite subnumber':11, 'duration':6,                                 'next frame':17},
  {'sprite number':50, 'sprite subnumber':12, 'duration':6,  'action pointer':"Fall",       'next frame':18},
  {'sprite number':50, 'sprite subnumber':12, 'duration':-1,                                'next frame':""}
)
States = {
  'initial frame': 0,
  'first moving frame': 1,
  'far attack frame': 7,
  'injury frame': 10,
  'death frame': 12
}
Flags = {
  'SOLID',
  'SHOOTABLE',
  'FLOAT',
  'NOGRAVITY'
}
