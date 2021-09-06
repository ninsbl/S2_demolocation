#!/bin/bash

#git checkout https://github.com/OSGeo/grass/blob/main/.github/workflows/ubuntu.yml
# https://github.com/marketplace/actions/update-files-on-github
# git checkout https://github.com/OSGeo/grass
# git checkout https://github.com/jhpoelen/zenodo-upload

# "https://zenodo.org/api/files/311ffb11-4ac1-4b6f-8c06-abf6ec70962f/S2_demolocation.tar.gz" \
grass --tmp-location XY --exec \
    g.download.location url="https://transfer.sh/J6K5fC/S2_demolocation.tar.gz" \
    path=.

grass --tmp-location XY --exec python3 setup_grass.py

grass --tmp-location XY --exec python3 get_scenes_list.py

ls scene_lists

git add scene_lists
git commit -m "update" scene_lists/*
git push origin main

grass ./S2_demolocation/epsg_25832/NBS --exec python3 build_strds.py
cd S2_demolocation
tar czf ../S2_demolocation.tar.gz epsg_25832
cd ..
zenodo_upload/zenodo_upload.sh 5458665 S2_demolocation.tar.gz