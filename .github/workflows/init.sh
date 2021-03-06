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

