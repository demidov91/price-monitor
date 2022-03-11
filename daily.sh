#! /bin/bash
cd ~/price-monitor/
../price-monitor-env/bin/python ~/price-monitor/run.py
../price-monitor-env/bin/python ~/price-monitor/analyze.py
git add .
git commit -m "Add data"
git push
