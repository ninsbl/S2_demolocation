#!/usr/bin/env python3

import grass.script as gscript

gscript.run_command("g.extension", url="https://github.com/ninsbl/m.crawl.thredds/archive/refs/heads/master.zip", extension="m.crawl.thredds")
gscript.run_command("g.extension", url="https://github.com/ninsbl/t.rast.import.netcdf/archive/refs/heads/master.zip", extension="t.rast.import.netcdf")

