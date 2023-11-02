#!/bin/sh -x
python3 -m build -o .
conf2spec conf.py -o main.spec
