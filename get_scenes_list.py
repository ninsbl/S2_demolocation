#!/usr/bin/env python3

from pathlib import Path
import grass.script as gscript
import os

directory = Path("./scene_lists")

if not directory.exists():
    directory.mkdir()

for instr in ["A", "B"]:
    print(f"{instr}")

    # DTERRENG data starts 2017
    for year in [2017, 2018, 2019, 2020, 2021]:
        print(f"{year}")
        scenes = gscript.read_command("m.crawl.thredds", 
                                  input=f"https://nbstds.met.no/thredds/catalog/NBS/S2{instr}/{year}/catalog.html",
                                  output=directory.joinpath(f"S2{instr}_{year}.txt"),
                                  filter=f".*DTERRENG.*",
                                  nprocs=50,
                                  overwrite=True)

