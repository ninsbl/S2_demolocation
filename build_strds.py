#!/usr/bin/env python3

gscript.run_command("g.region", res=10, flags="a")
for instr in ["A", "B"]:
    for proj in ["T31", "T32", "T33", "T34", "T35"]:
        gscript.run_command("t.rast.import.netcdf", input=f"S2{instr}_{proj}.txt", output="Sentinel_2", bandref="bandref.txt", flags="la{}".format("o" if proj == "T33" else ""), nodata="-1,65535", nprocs=20)
