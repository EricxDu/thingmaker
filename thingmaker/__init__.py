from . import main
from . import dehblocks

def get_framedefs(things, start=1):
  framedefs = []
  for number, thing in things.items():
    for n, frame in enumerate(thing.Frames):
      framedef = dehblocks.Frame(thing, start + n, n)
      framedefs.append(framedef)
    start += len(thing.Frames)
  return tuple(framedefs)

def get_thingdefs(things, start=1):
  thingdefs = []
  if not isinstance(things, dict):
    return tuple(thingdefs)
  for number, thing in things.items():
    thingdef = dehblocks.Thing(thing, number, start)
    if hasattr(thing, 'Frames'):
      start += len(thing.Frames)
    thingdefs.append(thingdef)
  return tuple(thingdefs)

def print_dehfile(*args, **kwargs):
  str_codeptr = "[codeptr]\n"
  str_strings = "[strings]\n"
  str_frames = "Patch File for DeHackEd v3.0\n"
  str_frames += "\n"
  str_frames += "# Note: Use the pound sign ('#') to start comment lines.\n"
  str_frames += "\n"
  str_frames += "Doom version = 19\n"
  str_frames += "Patch format = 6\n"
  str_frames += "\n"
  str_things = ""
  if 'start' in kwargs:
    n = kwargs['start']
  else:
    n = 1
  if 'indexed' in kwargs:
    for n, thing in kwargs['indexed'].items():
      _, new_frames, new_things, new_codeptrs, new_strings = main.get_thing(n, thing)
      str_frames += new_frames
      str_things += new_things
      str_codeptr += new_codeptrs
      str_strings += new_strings
  else:
    for thing in args:
      n, new_frames, new_things, new_codeptrs, new_strings = main.get_thing(n, thing)
      str_frames += new_frames
      str_things += new_things
      str_codeptr += new_codeptrs
      str_strings += new_strings
  print(str_frames + str_things + str_codeptr + "\n" + str_strings)
