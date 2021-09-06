#!/usr/bin/env python3

import grass.script as gscript

gscript.run_command("g.region", res=10, flags="a")
for instr in ["A", "B"]:
    for year in [2021]:
        for proj in ["T31", "T32", "T33", "T34", "T35"]:
            gscript.run_command("t.rast.import.netcdf",
                                input=directory.joinpath(f"S2{instr}_{year}_{proj}.txt"),
                                output="Sentinel_2",
                                bandref="bandref.txt",
                                flags="la{}".format("o" if proj == "T33" else ""),
                                nodata="-1,65535",
                                nprocs=20)
