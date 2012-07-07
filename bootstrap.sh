#!/bin/bash

CUR="`pwd`"
BASE_DIR=/opt/sw-python/pypkg
mkdir -p $BASE_DIR

virtualenv --no-site-packages $BASE_DIR/venv
. $BASE_DIR/venv/bin/activate
pip install -r requirements.txt
#cd $CUR
#python setup.py install
