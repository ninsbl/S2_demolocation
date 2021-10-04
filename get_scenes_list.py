#!/usr/bin/env python3

from pathlib import Path
import grass.script as gscript
import os

directory = Path("./scene_lists")

if not directory.exists():
    directory.mkdir()

instr = os.environ["S2_INSTRUMENT"]
print(f"{instr}")

# DTERRENG data starts 2017
for year in [2020]:
    print(f"{year}")
    for month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        print(f"{month:02}")
        scenes = gscript.read_command("m.crawl.thredds", 
                                  input=f"https://nbstds.met.no/thredds/catalog/NBS/S2{instr}/{year}/{month:02}/catalog.html",
                                  output=directory.joinpath(f"S2{instr}_{year}_{month:02}.txt"),
                                  filter=".*DTERRENG.*",
                                  skip=".*metadata.*,.*ql.*,.*jpeg.*,.*png.*",
                                  nprocs=50,
                                  overwrite=True)

