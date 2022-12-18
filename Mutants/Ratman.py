Type = "Thing"
Name = "Ratman"
Info = {
  'hit points': "100",
  'reaction time': "8",
  'pain chance': "256",
  'speed': "8",
  'width': "1048576",
  'height': "3670016",
  'mass': "50",
}
Frames = (
  {'sprite number':"38",'sprite subnumber':    "0",'duration':"10",'action pointer':      "Look",'next frame':   1},  #0
  {'sprite number':"38",'sprite subnumber':    "1",'duration':"10",'action pointer':      "Look",'next frame':   0},  #1
  {'sprite number':"38",'sprite subnumber':    "0",'duration': "3",'action pointer':     "Chase",'next frame':   3},  #2
  {'sprite number':"38",'sprite subnumber':    "0",'duration': "3",'action pointer':     "Chase",'next frame':   4},  #3
  {'sprite number':"38",'sprite subnumber':    "1",'duration': "3",'action pointer':     "Chase",'next frame':   5},  #4
  {'sprite number':"38",'sprite subnumber':    "1",'duration': "3",'action pointer':     "Chase",'next frame':   6},  #5
  {'sprite number':"38",'sprite subnumber':    "2",'duration': "3",'action pointer':     "Chase",'next frame':   7},  #6
  {'sprite number':"38",'sprite subnumber':    "2",'duration': "3",'action pointer':     "Chase",'next frame':   8},  #7
  {'sprite number':"38",'sprite subnumber':    "3",'duration': "3",'action pointer':     "Chase",'next frame':   9},  #8
  {'sprite number':"38",'sprite subnumber':    "3",'duration': "3",'action pointer':     "Chase",'next frame':   2},  #9
  {'sprite number':"38",'sprite subnumber':    "4",'duration':"10",'action pointer':"FaceTarget",'next frame':  11},  #10
  {'sprite number':"38",'sprite subnumber':"32773",'duration': "4",'action pointer':"SPosAttack",'next frame':  12},  #11
  {'sprite number':"38",'sprite subnumber':    "4",'duration': "6",'action pointer':"FaceTarget",'next frame':  13},  #12
  {'sprite number':"38",'sprite subnumber':"32773",'duration': "4",'action pointer':"SPosAttack",'next frame':  14},  #13
  {'sprite number':"38",'sprite subnumber':    "4",'duration': "1",'action pointer':"SpidRefire",'next frame':  10},  #14
  {'sprite number':"38",'sprite subnumber':    "6",'duration': "3",                              'next frame':  16},  #15
  {'sprite number':"38",'sprite subnumber':    "6",'duration': "3",'action pointer':      "Pain",'next frame':   2},  #16
  {'sprite number':"38",'sprite subnumber':    "7",'duration': "5",                              'next frame':  18},  #17
  {'sprite number':"38",'sprite subnumber':    "8",'duration': "5",'action pointer':    "Scream",'next frame':  19},  #18
  {'sprite number':"38",'sprite subnumber':    "9",'duration': "5",'action pointer':      "Fall",'next frame':  20},  #19
  {'sprite number':"38",'sprite subnumber':   "10",'duration': "5",                              'next frame':  21},  #20
  {'sprite number':"38",'sprite subnumber':   "11",'duration': "5",                              'next frame':  22},  #21
  {'sprite number':"38",'sprite subnumber':   "12",'duration':"-1",                              'next frame':None},  #22
)
States = {
  'initial frame': 0,
  'first moving frame': 2,
  'far attack frame': 10,
  'injury frame': 15,
  'death frame': 17
}
Flags = {
  'SOLID',
  'SHOOTABLE',
  'COUNTKILL'
}
