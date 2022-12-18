Thingmaker for Boom
===================

Thingmaker utilizes the DeHackEd file format to completely rebuild
Boom's state table and Thing state references. You can write an
individual Python file for each Thing you want in the game, and
Thingmaker will write a DeHackEd lump that lists all of the state
frames in order and references them with corresponding Thing
definitions. It even builds a codeptr table and identifies everything
with a comment for easy reading and reference.

Thingmaker provides some example Things along with brand-new monster
sprites by [Paul Zarczynski](https://paul.drdteam.org/) retrieved from
[OpenGameArt](https://opengameart.org/users/nmn).


Instructions
------------

You'll need Python3, DeuTeX, and a Boom source port.  You may also
need a doom2.wad or freedoom2.wad somewhere on your PATH. The
following commands will construct the dehacked lump, create the PWAD,
and start Boom with the PWAD.

    python setup_mutants.py > lumps/dehacked.lmp
    deutex -make mutants.wad
    boom -file mutants.wad

If you make any changes, you'll need to delete the created PWAD so
that DeuTeX can replace it with a new one. Or just choose a new name
for the new PWAD.

    rm mutants.wad


Work-In-Progress
----------------

Thingmaker is currently in pre-Alpha development stage. Function
names, parameter order, and everything else are subject to change as
the package is prepared for commercial release.


Other Goals
-----------

Heavily modifying the state table can have some unintended effects,
many of which aren't documented in any readily-available material
about DeHackEd/BEX. During development Thingmaker will discover and
document as many of these bugs as possible, as well as link to and
archive existing documentation when available.


Notes/Bugs/Todo
---------------

There are some hard-coded entry points into the state table that must
be kept in mind.

- A_FirePlasma uses the frame directly after the weapon's
  'firing frame' so this must be reserved.
