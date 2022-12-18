mobjinfo_t = {
  'doomednum': "ID #",
  'spawnstate': "initial frame",
  'spawnhealth': "hit points",
  'seestate': "first moving frame",
  'seesound': "alert sound",
  'reactiontime': "reaction time",
  'attacksound': "attack sound",
  'painstate': "injury frame",
  'painchance': "pain chance",
  'painsound': "pain sound",
  'meleestate': "close attack frame",
  'missilestate': "far attack frame",
  'deathstate': "death frame",
  'xdeathstate': "exploding frame",
  'deathsound': "death sound",
  'speed': "speed",
  'radius': "width",
  'height': "height",
  'mass': "mass",
  'damage': "missile damage",
  'activesound': "action sound",
  'flags': "bits",
  'raisestate': "respawn frame"
}
state_t = {
  'sprite': "sprite number",
  'frame': "sprite subnumber",
  'tics': "duration",
  'action': "#action pointer",
  'nextstate': "next frame",
  'misc1': "unknown 1",
  'misc2': "unknown 2"
}

def Translation(definitions, translations):
  for key in definitions.keys() & translations.keys():
    definitions[translations[key]] = definitions.pop(key)
  return definitions
