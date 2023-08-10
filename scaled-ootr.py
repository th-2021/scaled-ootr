import glob
import json
import os
import pyvips

source = './OoT-Reloaded-SoH/OoT Reloaded (SoH)'
target = './new/'

with open(source + "/manifest.json", "r") as manifest_file:
  manifest = json.load(manifest_file)

png_list = glob.glob('**/*.png', root_dir=source, recursive=True)

for png in png_list:
    image = pyvips.Image.new_from_file(source + "/" + png, access='random')
    png_noext = os.path.splitext(png)[0]
    try:
      info = manifest[png_noext]

      print(png)
      print(info)

      height_factor = info["textureHeight"]*4 / image.height
      width_factor = info["textureWidth"]*4 / image.width
      image = image.affine((width_factor, 0, 0, height_factor))
      os.makedirs(target + os.path.dirname(png), exist_ok=True)

      image.write_to_file(target + png)
    except KeyError:
      print(f"{png_noext} is unknown.")
