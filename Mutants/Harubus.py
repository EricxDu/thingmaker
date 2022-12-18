Type = "Thing"
Name = "Harubus"
Info = {
  'hit points': "600",
  'reaction time': "8",
  'pain chance': "80",
  'speed': "8",
  'width': "3145728",
  'height': "4194304",
  'mass': "1000",
  'alert sound': "49",
  'action sound': "75",
  'pain sound': "29",
  'death sound': "100"
}
Frames = (
  {'sprite number':"37", 'sprite subnumber':"0",     'duration':"15", 'action pointer':"Look",       'next frame':1 },
  {'sprite number':"37", 'sprite subnumber':"1",     'duration':"15", 'action pointer':"Look",       'next frame':0 },
  {'sprite number':"37", 'sprite subnumber':"0",     'duration':"4",  'action pointer':"Chase",      'next frame':3 },
  {'sprite number':"37", 'sprite subnumber':"0",     'duration':"4",  'action pointer':"Chase",      'next frame':4 },
  {'sprite number':"37", 'sprite subnumber':"1",     'duration':"4",  'action pointer':"Chase",      'next frame':5 },
  {'sprite number':"37", 'sprite subnumber':"1",     'duration':"4",  'action pointer':"Chase",      'next frame':6 },
  {'sprite number':"37", 'sprite subnumber':"2",     'duration':"4",  'action pointer':"Chase",      'next frame':7 },
  {'sprite number':"37", 'sprite subnumber':"2",     'duration':"4",  'action pointer':"Chase",      'next frame':8 },
  {'sprite number':"37", 'sprite subnumber':"3",     'duration':"4",  'action pointer':"Chase",      'next frame':9 },
  {'sprite number':"37", 'sprite subnumber':"3",     'duration':"4",  'action pointer':"Chase",      'next frame':10},
  {'sprite number':"37", 'sprite subnumber':"4",     'duration':"4",  'action pointer':"Chase",      'next frame':11},
  {'sprite number':"37", 'sprite subnumber':"4",     'duration':"4",  'action pointer':"Chase",      'next frame':12},
  {'sprite number':"37", 'sprite subnumber':"5",     'duration':"4",  'action pointer':"Chase",      'next frame':13},
  {'sprite number':"37", 'sprite subnumber':"5",     'duration':"4",  'action pointer':"Chase",      'next frame':2 },
  {'sprite number':"37", 'sprite subnumber':"6",     'duration':"20", 'action pointer':'FatRaise',   'next frame':15},
  {'sprite number':"37", 'sprite subnumber':"32775", 'duration':"10", 'action pointer':'FatAttack1', 'next frame':16},
  {'sprite number':"37", 'sprite subnumber':"8",     'duration':"5",  'action pointer':"FaceTarget", 'next frame':17},
  {'sprite number':"37", 'sprite subnumber':"6",     'duration':"5",  'action pointer':"FaceTarget", 'next frame':18},
  {'sprite number':"37", 'sprite subnumber':"32775", 'duration':"10", 'action pointer':'FatAttack2', 'next frame':19},
  {'sprite number':"37", 'sprite subnumber':"8",     'duration':"5",  'action pointer':"FaceTarget", 'next frame':20},
  {'sprite number':"37", 'sprite subnumber':"6",     'duration':"5",  'action pointer':"FaceTarget", 'next frame':21},
  {'sprite number':"37", 'sprite subnumber':"32775", 'duration':"10", 'action pointer':'FatAttack3', 'next frame':22},
  {'sprite number':"37", 'sprite subnumber':"8",     'duration':"5",  'action pointer':"FaceTarget", 'next frame':23},
  {'sprite number':"37", 'sprite subnumber':"6",     'duration':"5",  'action pointer':"FaceTarget", 'next frame':2 },
  {'sprite number':"37", 'sprite subnumber':"9",     'duration':"3",                                 'next frame':25},
  {'sprite number':"37", 'sprite subnumber':"9",     'duration':"3",  'action pointer':"Pain",       'next frame':2 },
  {'sprite number':"37", 'sprite subnumber':"10",    'duration':"6",                                 'next frame':27},
  {'sprite number':"37", 'sprite subnumber':"11",    'duration':"6",  'action pointer':"Scream",     'next frame':28},
  {'sprite number':"37", 'sprite subnumber':"12",    'duration':"6",  'action pointer':"Fall",       'next frame':29},
  {'sprite number':"37", 'sprite subnumber':"13",    'duration':"6",                                 'next frame':30},
  {'sprite number':"37", 'sprite subnumber':"14",    'duration':"6",                                 'next frame':31},
  {'sprite number':"37", 'sprite subnumber':"15",    'duration':"6",                                 'next frame':32},
  {'sprite number':"37", 'sprite subnumber':"16",    'duration':"6",                                 'next frame':33},
  {'sprite number':"37", 'sprite subnumber':"17",    'duration':"6",                                 'next frame':34},
  {'sprite number':"37", 'sprite subnumber':"18",    'duration':"6",                                 'next frame':35},
  {'sprite number':"37", 'sprite subnumber':"19",    'duration':"-1", 'action pointer':'BossDeath',  'next frame':""}
)
States = {
  'initial frame': 0,
  'first moving frame': 2,
  'far attack frame': 15,
  'injury frame': 24,
  'death frame': 26
}
Flags = {
  'SOLID',
  'SHOOTABLE',
  'COUNTKILL'
}
