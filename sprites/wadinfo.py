import os

from PIL import Image

STANDERS = ("boss", "bos2", "cpos", "cybr", "fatt", "play", "poss", "sarg",
  "skel", "spos", "sswv", "troo")
POWERUPS = ('soul')

for filename in sorted(os.listdir( )):
  name, ext = os.path.splitext(filename)
  if not ext in (".png", ".gif", ".tif", ".ppm"):
    continue
  image = Image.open(filename)
  (width, height) = image.size
  if name[:4] in STANDERS:
    x_offset = int( width / 2 )
    y_offset = height - 5
  elif name[:4] in POWERUPS:
    x_offset = int( width / 2 )
    y_offset = int( height * 1.5 )
  else:
    x_offset = int( width / 2 )
    y_offset = height
  print(name + "\t" + str(x_offset) + "\t" + str(y_offset))
  rgba = image.convert("RGBA")
  datas = rgba.getdata()
  if datas[0][3] == 0:
    continue
  new_data = []
  for pixel in datas:
    if pixel == (0, 255, 255, 255):
      new_data.append((0, 0, 0, 0))
    else:
      new_data.append(pixel)
  rgba.putdata(new_data)
  rgba.save(name.lower() + ".png", "PNG")
