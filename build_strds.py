#!/usr/bin/env python3

from pathlib import Path
import re
import subprocess

import grass.script as gscript


gscript.run_command("t.connect", flags="d")

directory = Path("./scene_lists")

tmp_file = Path("./tmp.txt")

infile = sorted(list(directory.glob("*.txt")))
if not infile:
    sys.exit("No scene list found")

infile = infile[0]

print(infile)
# Regular expression for tiles over Norway
re_str = ".*_T(31VFL|32VKL|32VKM|32VKN|32VKP|32VKQ|32VLK|32VLL|32VLM|32VLN|32VLP|32VLQ|32VLR|32VMK|32VML|32VMM|32VMN|32VMP|32VMQ|32VMR|32VNK|32VNL|32VNM|32VNN|32VNP|32VNQ|32VNR|32VPL|32VPM|32VPN|32VPP|32VPQ|32VPR|32WNS|32WNT|32WPA|32WPB|32WPS|32WPT|32WPU|32WPV|33VUF|33VUG|33VUH|33VUJ|33VUK|33VUL|33VVL|33WVM|33WVN|33WVP|33WVQ|33WVR|33WVS|33WWP|33WWQ|33WWR|33WWS|33WWT|33WXR|33WXS|33WXT|34WDA|34WDB|34WDC|34WDD|34WEB|34WEC|34WED|34WFB|34WFC|34WFD|34WFE|35WLV|35WMS|35WMT|35WMU|35WMV|35WNS|35WNT|35WNU|35WPT|35WPU).*"

# Set region
gscript.message("processing {}".format(infile))
#filter, write to tmp file, use tmpfile as input
scenes = infile.read_text().split("\n")
if scenes:
    for proj in ["T31", "T32", "T33", "T34", "T35"]:
        rel_scenes = [scene for scene in scenes if f"_{proj}" in scene]
        if rel_scenes:
            # Filter scenes over Norway
            rel_scenes = [scene for scene in rel_scenes if re.match(re_str, scene)]
            if rel_scenes:
                # Use only latest file for each scene
                scene_ids = set([re.findall(".*?_T....._", scene)[0].rstrip("_") for scene in rel_scenes])
                rel_scenes = [sorted([scene for scene in rel_scenes if scene_id in scene], reverse=True)[0] for scene_id in scene_ids]
                if rel_scenes:
                    tmp_file.write_text("\n".join(rel_scenes))
                    # Import relevant scenes
                    gscript.run_command("t.rast.import.netcdf",
                                        input=tmp_file,
                                        output="Sentinel_2_DTERRENG",
                                        bandref="bandref.txt",
                                        flags="la{}".format("o" if proj == "T33" else ""),
                                        nodata="-1,65535",
                                        nprocs=20,
                                        verbose=True)
            else:
                gscript.message("No DTERRENG scenes with projection {} over Norway in {}".format(proj, str(infile)))
        else:
            gscript.message("No DTERRENG scenes with projection {} in {}".format(proj, str(infile)))
else:
    gscript.message("No DTERRENG scenes in {}".format(str(infile)))

gscript.message("Done processing {}".format(infile))

# move fully processed file with scenes
subprocess.run(["git", "mv", str(infile), str(directory.joinpath("processed", infile.name))])

# remove tmp file
tmp_file.unlink()
