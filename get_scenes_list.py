for instr in ["A", "B"]:
    for proj in ["T29", "T30", "T31", "T32", "T33", "T34", "T35"]:
        scenes = gscript.read_command("m.crawl.thredds", url="https://{}.xml".format(instr), filter=".*{}.*DTERRENG.*".format(proj), nprocs=10)
        with open(f"S2{instr}_{proj}.txt", "a") as scene_list:
            scene_list.write(scenes)
