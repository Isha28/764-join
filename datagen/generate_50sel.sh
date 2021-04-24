#!/bin/sh

echo "Generating build side..."
python genbuild_50sel.py > 016M_build.tbl
echo "Generating probe side..."
python genprobe.py > 256M_probe.tbl
