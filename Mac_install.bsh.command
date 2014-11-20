#!/bin/bash

echo "Starting Install"

BASEDIR=$(dirname $0)

echo "Please type in your password to proceed with installation"

sudo easy_install mechanize

python $BASEDIR\\Dist\\Midd_Script.py