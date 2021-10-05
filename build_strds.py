#!/usr/bin/env python3

from pathlib import Path

import grass.script as gscript

gscript.run_command("t.connect", flags="d")

directory = Path("./scene_lists")

tmp_file = Path("./tmp.txt")

# Set region
for instr in ["A", "B"]:
    for year in [2018]:
        for proj in ["T31", "T32", "T33", "T34", "T35"]:
            for month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                print(f"S2{instr} {year} {month:02}")
                infile = directory.joinpath(f"S2{instr}_{year}_{month:02}.txt")
                if not infile.exists():
                    print("{} not found".format(str(infile)))
                    continue

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
                    print("No DTERRENG scenes in {}".format(str(infile)))

