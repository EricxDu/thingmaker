import thingmaker
from Mutants import Grell
from Mutants import Fireball6
from Mutants import Harubus, Wargrin, Droid, Bug, StabilityOfficer
from Mutants import SuperWargrin
from Mutants import Hindring
from Mutants import Enforcer
from Mutants import BionicMonkey
from Mutants import Ratman
from Mutants import Fireball7
from Mutants import Outcast
from Mutants import Outleader
from Mutants import TechLamp1
from Mutants import TechLamp2
from Mutants import Chair

#it's potentially buggy to leave Thing numbers unchanged
#if they are placed on a map or spawned by a function they may refer
#to unintended entries in the state table
things = {
  2: StabilityOfficer,
  3: Enforcer,
  4: Chair,
  #Fire
  6: Droid,
  #Tracer
  #Smoke
  9: Harubus,
  10: Fireball6,
  11: Ratman,
  12: Wargrin,
  13: Hindring,
  14: BionicMonkey,
  15: Bug,
  16: Outleader,
  17: Fireball7,
  18: Outcast,
  19: Grell,
  #Spider
  #Baby
  #Cyborg
  #Pain
  #WolfSS
  80: TechLamp1,
  81: TechLamp2
}
framedefs = thingmaker.get_framedefs(things, start=174)
thingdefs = thingmaker.get_thingdefs(things, start=174)
codeptr = thingmaker.dehblocks.Codeptr(things, start=174)
strings = thingmaker.dehblocks.Strings(things)
frame_section = "\n\n".join(framedefs)
thing_section = "\n\n".join(thingdefs)
print("\n\n".join((frame_section, thing_section, codeptr, strings)))
