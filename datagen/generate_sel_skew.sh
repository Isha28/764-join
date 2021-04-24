#!/bin/sh

echo "Generating build side..."
python genbuild_sel_skew.py > 016M_build.tbl
echo "Generating probe side..."
python genprobe_sel_skew.py > 256M_probe.tbl
