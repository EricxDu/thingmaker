CC_STRINGS = {
  1: "CC_HERO",
  2: "CC_ZOMBIE",
  3: "CC_SHOTGUN",
  4: "CC_VILE",
  6: "CC_REVEN",
  9: "CC_MANCU",
  11: "CC_HEAVY",
  12: "CC_IMP",
  13: "CC_DEMON",
  15: "CC_CACO",
  16: "CC_BARON",
  18: "CC_HELL",
  19: "CC_LOST",
  20: "CC_SPIDER",
  21: "CC_ARACH",
  22: "CC_CYBER",
  23: "CC_PAIN"
}
DEFAULT_INFO = {
  'hit points': 1000,
  'reaction time': 8,
  'pain chance': 0,
  'speed': 0,
  'width': 1310720,  #40MU
  'height': 1048576,  #32MU 
  'mass': 100,
  'alert sound': 0,
  'attack sound': 0,
  'pain sound': 0,
  'death sound': 0,
  'action sound': 0
}
DEFAULT_STATES = {
  'initial frame': 0,  #first relative state of thing
  'first moving frame': "0",  #null state of state table
  'injury frame': "0",
  'close attack frame': "0",
  'far attack frame': "0",
  'death frame': "0",
  'exploding frame': "0",
  'respawn frame': "0"
}
DEFAULT_FLAGS = {'0',}
DEFAULT_FRAME = {
  'sprite number': "0",
  'sprite subnumber': "0",
  'duration': "-1",
  'action pointer': "Null",
  'next frame': "0",
  'unknown 1': "0",
  'unknown 2': "0"
}

def Bits():
  """
  iterate list of numbers and strings
  if number, OR the individual bit flags
    turn each bit flag into a string
    remove number, insert strings
  join the resulting list with + dividers
  """

def Declaration(identifier, number, comment=None):
  if comment:
    comment = "".join(( "(", comment, ")" ))
    number = " ".join(( str(number), comment ))
  return " ".join(( str(identifier), str(number) ))

def Statement(key, value, comment=None):
  if comment:
    value = "  #".join(( str(value), str(comment) ))
  return " = ".join(( str(key), str(value) ))

def _identifyState(thing, n):
  name = "?"
  if hasattr(thing, 'Number'):
    name = " ".join(( "thing", str(thing.Number) ))
  if hasattr(thing, 'Name'):
    name = thing.Name
  state = " ".join(( "frame", str(n + 1) ))
  for key, value in thing.States.items():
    if value == n:
      state = " ".join(( key, str(n + 1) ))
  return " ".join(( name, state ))

def _getActions(thing):
  codeptrs = []
  if not hasattr(thing, 'Frames'):
    return codeptrs
  for state in thing.Frames:
    if 'action pointer' in state:
      codeptrs.append(state['action pointer'])
    else:
      codeptrs.append('Null')
  return codeptrs

def Codeptr(things, start=1):
  lines = ["[codeptr]",]  #return at least this
  n = start
  for thing in things.values():
    if not hasattr(thing, 'Frames'):
      continue
    for f, frame in enumerate(thing.Frames):
      value = "Null"
      if 'action pointer' in frame:
        value = frame['action pointer']
      key = " ".join(( "frame", str(n) ))
      statement = Statement(key, value)
      if hasattr(thing, 'Name'):
        comment = _identifyState(thing, f)
        statement = Statement(key, value, comment)
      lines.append(statement)
      n = n + 1
  return "\n".join( lines )
      
def Frame(thing, number, index=0):
  line0 = Declaration("Frame", number)
  if hasattr(thing, 'Name'):
    comment = _identifyState(thing, index)
    line0 = Declaration("Frame", number, comment)
  frame = DEFAULT_FRAME | thing.Frames[index]
  lines = [line0]
  for key, value in frame.items():
    if key == 'next frame':
      if isinstance(value, int):
        value = number - index + value
      else:
        value = 0
    if key == 'action pointer':
      key = '#action pointer'
    lines.append(Statement( key, value ))
  block = "\n".join( lines )
  return block

def Strings(things):
  lines = ["[strings]",]
  if isinstance(things, dict):
    for number, thing in things.items():
      if not number in CC_STRINGS:
        continue
      if not hasattr(thing, 'Name'):
        continue
      lines.append(Statement( CC_STRINGS[number], thing.Name ))
  return "\n".join( lines )

def Thing(thing, number=1, start=1):
  if not hasattr(thing, 'Type'):
    return " ".join( ("Nothing", "0" ) )
  line0 = Declaration(thing.Type, number, thing.Name)
  info = DEFAULT_INFO.copy()
  states = DEFAULT_STATES.copy()
  flags = DEFAULT_FLAGS.copy()
  if (hasattr(thing, 'Info') and isinstance(thing.Info, dict)):
    info = info | thing.Info
  if (hasattr(thing, 'States') and isinstance(thing.States, dict)):
    states = states | thing.States
    for key, value in states.items():
      if isinstance(value, int) and isinstance(start, int):
        states[key] = value + start
  if hasattr(thing, 'Flags'):
    flags = thing.Flags - flags
  lines = [line0]
  for key, value in info.items():
    lines.append(Statement( key, value ))
  for key, value in states.items():
    lines.append(Statement( key, value ))
  flags = "+".join(flags)
  lines.append(Statement( "bits", flags ))
  return "\n".join( lines )
