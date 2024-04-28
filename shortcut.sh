#!/usr/bin/env bash

cd ~/Projects/eat40005/worklog
FILENAME="txts/week-$1.txt"
touch $FILENAME 
mousepad $FILENAME
nix-shell

FILENAME="export/102874485_week-$1.pdf"
evince $FILENAME &
cp $FILENAME ~/Downloads/.

