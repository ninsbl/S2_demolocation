#!/usr/bin/env python3

from pathlib import Path
import grass.script as gscript

directory = Path("./scene_lists")

if not directory.exists():
    directory.mkdir()

for instr in ["A", "B"]:
    print(f"Sentinel-2{instr}")
    for year in [2021]:
        print(f"{year}")
        for proj in ["T31", "T32", "T33", "T34", "T35"]:
            print(f"{proj}")
            scenes = gscript.read_command("m.crawl.thredds", url=f"https://nbstds.met.no/thredds/catalog/NBS/S2{instr}/{year}/catalog.html", filter=f".*{proj}.*DTERRENG.*", nprocs=10)
            with open(directory.joinpaths(f"S2{instr}_{year}_{proj}.txt"), "w") as scene_list:
                scene_list.write(scenes)

