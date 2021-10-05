#!/bin/bash

# grass --tmp-location XY --exec python3 get_scenes_list.py

# ls scene_lists

#git add scene_lists
#git commit -m "update" scene_lists/*
#git push origin main

grass epsg_25833/NBS_DTERRENG --exec python3 build_strds.py

#cd S2_demolocation
#tar czf ../S2_demolocation.tar.gz epsg_25832
#cd ..
#zenodo_upload/zenodo_upload.sh 5458665 S2_demolocation.tar.gz
