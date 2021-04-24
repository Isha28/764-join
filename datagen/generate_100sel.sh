#!/bin/sh

echo "Generating build side..."
python genbuild_100sel.py > 016M_build.tbl
echo "Generating probe side..."
python genprobe.py > 256M_probe.tbl
