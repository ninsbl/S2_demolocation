#!/usr/bin/env python3

from pathlib import Path
import grass.script as gscript
import os

directory = Path("./scene_lists")

if not directory.exists():
    directory.mkdir()

instr = os.environ["S2_NSTRUMENT"]
proj = os.environ["S2_PROJ"]
year = os.environ["S2_YEAR"]

print(f"Sentinel-2{instr}")
print(f"{proj}")

# DTERRENG data starts 2017
for year in [2017, 2018, 2019, 2020, 2021]:
    print(f"{year}")
    scenes = gscript.read_command("m.crawl.thredds", 
                              input=f"https://nbstds.met.no/thredds/catalog/NBS/S2{instr}/{year}/catalog.html",
                              output=directory.joinpath(f"S2{instr}_{year}_{proj}.txt"),
                              filter=f".*{proj}.*DTERRENG.*",
                              nprocs=200)

