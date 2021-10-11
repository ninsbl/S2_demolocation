#!/usr/bin/env python3

from pathlib import Path
import grass.script as gscript
import subprocess


gscript.run_command("t.connect", flags="d")

directory = Path("./scene_lists")

tmp_file = Path("./tmp.txt")

infile = sorted(list(directory.glob("*.txt")))
if not infile:
    sys.exit("No scene list found")

infile = infile[0]

print(infile)

# Set region
for proj in ["T31", "T32", "T33", "T34", "T35"]:
    print(infile, proj)

    #filter, write to tmp file, use tmpfile as input
    scenes = infile.read_text().split("\n")
    print(scenes)
    rel_scenes = [scene for scene in scenes if f"_{proj}" in scene]
    if rel_scenes:
        tmp_file.write_text("\n".join(rel_scenes))
        # Import relevant scenes
        gscript.run_command("t.rast.import.netcdf",
                            input=tmp_file,
                            output="Sentinel_2_DTERRENG",
                            bandref="bandref.txt",
                            flags="la{}".format("o" if proj == "T33" else ""),
                            nodata="-1,65535",
                            nprocs=20,
                            verbose=True)
    else:
        print("No DTERRENG scenes with projection {} in {}".format(proj, str(infile)))

print("Done processing {}".format(infile))

# move fully processed file with scenes
subprocess.run(["git", "mv", str(infile), str(directory.joinpath("processed", infile.name))])
# remove tmp file
tmp_file.unlink()
