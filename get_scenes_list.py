#!/usr/bin/env python3

from pathlib import Path
import grass.script as gscript
import os

directory = Path("./scene_lists")

if not directory.exists():
    directory.mkdir()

#instr = os.environ["S2_NSTRUMENT"]
proj = os.environ["S2_PROJ"]
#year = os.environ["S2_YEAR"]

print(f"{proj}")

# DTERRENG data starts 2017
for year in [2017, 2018, 2019, 2020, 2021]:
    print(f"{year}")
    scenes = gscript.read_command("m.crawl.thredds", 
                              input=f"https://nbstds.met.no/thredds/catalog/NBS/S2A/{year}/catalog.html",
                              output=directory.joinpath(f"S2A_{year}_{proj}.txt"),
                              filter=f".*{proj}.*DTERRENG.*",
                              nprocs=100,
                              overwrite=True)
    scenes = gscript.read_command("m.crawl.thredds", 
                              input=f"https://nbstds.met.no/thredds/catalog/NBS/S2B/{year}/catalog.html",
                              output=directory.joinpath(f"S2B_{year}_{proj}.txt"),
                              filter=f".*{proj}.*DTERRENG.*",
                              nprocs=100,
                              overwrite=True)

