from .const import CC_STRINGS

def get_thing(start, thing):
  str_frames = ""
  str_things = "Thing " + str(thing.number)
  str_things = str_things + " (" + thing.name + ")\n"
  if hasattr(thing, 'stats'):
    for key in thing.stats:
      str_things = str_things + key + " = "
      str_things = str_things + str(thing.stats[ key ]) + "\n"
  str_codeptr = ""
  if thing.number in CC_STRINGS:
    str_ccstring = CC_STRINGS[thing.number] + " = " + thing.name + "\n"
  else:
    str_ccstring = ""
  n = start
  names = {}
  if hasattr(thing, 'states'):
    for state in thing.states:
      str_frames += "Frame " + str(n) + " (" + thing.name
      if 'thingmaker_named_frame' in state:
        names[state['thingmaker_named_frame']] = n
        str_frames += " " + state['thingmaker_named_frame']
        str_things += state['thingmaker_named_frame'] + " = " + str(n) + "\n"
      str_frames += ")\n"
      str_frames += get_frame(state, names, n)
      str_frames += "\n"
      str_codeptr += "frame " + str(n) + " = "
      if 'action pointer' in state:
        str_codeptr += state['action pointer']
      else:
        str_codeptr += "Null"
      if 'thingmaker_named_frame' in state:
        str_codeptr += "  #" + thing.name
        str_codeptr += " " + state['thingmaker_named_frame']
      str_codeptr += "\n"
      n = n + 1
  str_things += "\n"
  return n, str_frames, str_things, str_codeptr, str_ccstring

def str_named_framenum(n, name, keys):
  try:
    relative = int(name)
    return str(n + relative) + "\n"
  except:
    if name in keys:
      return str(keys[name]) + "  #" + name + "\n"
    else:
      return "0  #named state not found\n"

def get_frame(state, names, n):
  str_frame = ""
  for key in state:
    if key == 'action pointer':
      #leave blank if not a string
      if isinstance(state[key], str):
        #comment out because action pointers go in [codeptr] section
        str_frame += "#action pointer = " + state[key] + "\n"
    elif isinstance(state[key], str):
      if not key == 'thingmaker_named_frame':
        #find relative frame number or named frame
        str_frame += key + " = " + str_named_framenum(n, state[key], names)
    else:
      str_frame += key + " = " + str(state[key]) + "\n"
  if 'next frame' not in state:
    str_frame += "next frame = " + str(n + 1) + "\n"
  return str_frame
