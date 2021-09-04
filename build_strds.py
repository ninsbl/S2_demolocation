gscript.run_command("g.region", res=10, flags="a")
for instr in ["A", "B"]:
    for proj in ["T29", "T30", "T31", "T32", "T33", "T34", "T35"]:
        gscript.run_command("t.rast.import.netcdf", input=f"S2{instr}_{proj}.txt", output="Sentinel_2_NBS", bandref="", flags="loa", nprocs=10)
