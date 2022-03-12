#!/bin/bash
echo ""
echo ""
echo "Start to calculation model ..."
python3 -m cProfile -s time  main.py > prof_full.txt
sed '22,$d' prof_full.txt > prof_small.txt
echo ""
echo ""
echo ""
