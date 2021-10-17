# S2_demolocation
Scripts to build (and update) a GRASS GIS demo location with a SpaceTimeRasterDataSet (STRDS) containing Sentinel-2 scenes from the Norwegian ground segment (NBS).

In general, Sentiel-2 data will only be linked, so the size (in terms of MB) of the location will be limited even with hundrets of scenes in one STRDS.

Next steps would be to patch scenes based on their temporal granules, with one virtual raster per granule.
For patched maps, processing examples (pre-procssing, gap-filling...) could be prepared.

Another demo example could cover a smaller area but downloaded data for a subset, so once the location is available, network connection is no longer required... 
