#!/bin/bash

#git checkout https://github.com/OSGeo/grass/blob/main/.github/workflows/ubuntu.yml
# https://github.com/marketplace/actions/update-files-on-github
# git checkout https://github.com/OSGeo/grass
# git checkout https://github.com/jhpoelen/zenodo-upload

grass --tmp-location XY --exec \
    g.download.location url="https://zenodo.org/api/files/311ffb11-4ac1-4b6f-8c06-abf6ec70962f/S2_demolocation.tar.gz" \
    path=.

grass --tmp-location XY --exec python3 setup_grass.py

grass --tmp-location XY --exec python3 list_nc.py

ls

grass ./epsg_25832/NBS --exec python3 build_strds.py
tar czf S2_demolocation.tar.gz epsg_25832
zenodo_upload/zenodo_upload.sh 5458665 S2_demolocation.tar.gz