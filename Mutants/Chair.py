Type = "Thing"
Name = "Office Chair"
Info = {
  'hit points': "1000",
  'reaction time': "8",
  'pain chance': "255",
  'width': "1310720",
  'height': "1048576",
  'mass': "100"
}
Frames = (
  {'sprite number':"117", 'sprite subnumber':"0", 'duration':"-1",                                            'next frame':1},
  {'sprite number':"117", 'sprite subnumber':"0", 'duration':"4",  'action pointer':'Turn', 'unknown 1':"60", 'next frame':2},
  {'sprite number':"117", 'sprite subnumber':"0", 'duration':"6",  'action pointer':'Turn', 'unknown 1':"50", 'next frame':3},
  {'sprite number':"117", 'sprite subnumber':"0", 'duration':"8",  'action pointer':'Turn', 'unknown 1':"40", 'next frame':4},
  {'sprite number':"117", 'sprite subnumber':"0", 'duration':"10", 'action pointer':'Turn', 'unknown 1':"30", 'next frame':5},
  {'sprite number':"117", 'sprite subnumber':"0", 'duration':"12", 'action pointer':'Turn', 'unknown 1':"20", 'next frame':0}
)
States = {
  'initial frame': 0,
  'injury frame': 1
}
Flags = {
  'SOLID',
  'SHOOTABLE',
  'DROPOFF',
  'BOUNCES',
  'NOBLOOD'
}
