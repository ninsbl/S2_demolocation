#!/usr/bin/env python3

from pathlib import Path

import grass.script as gscript

directory = Path("./scene_lists")

tmp_file = Path("./tmp.txt")

# Set region
for instr in ["A", "B"]:
    for year in [2017]:
        for proj in ["T31", "T32", "T33", "T34", "T35"]:
            for month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                infile = directory.joinpath(f"S2{instr}_{year}_{month}.txt")
                if not infile.exists():
                    continue

                #filter, write to tmp file, use tmpfile as input
                scenes = infile.read_text().split("\n")
                rel_scenes = [scene for scene in scenes if f"_{proj}" in scene]
                if rel_scenes:
                    tmp_file.write(rel_scenes)
                    # Import relevant scenes
                    gscript.run_command("t.rast.import.netcdf",
                                        input=tmp_file,
                                        output="Sentinel_2_DTERRENG",
                                        bandref="bandref.txt",
                                        flags="la{}".format("o" if proj == "T33" else ""),
                                        nodata="-1,65535",
                                        nprocs=20)

