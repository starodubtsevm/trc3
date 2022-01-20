#!/bin/bash
echo ""
echo ""
echo "Start to calculation coefficients ..."
echo ""
python3 '../gen_filters/main.py'
echo ""
echo ""
echo "Start to calculation model ..."
echo ""
echo ""
python3 '../trc3_model/main.py' 

