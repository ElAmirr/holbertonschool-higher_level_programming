#!/bin/bash
python3.4 - m py_compile $PYFILE
mv __pycache__/*pyc $PYFILE'c'
