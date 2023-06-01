#!/bin/bash

echo "Content-type:text/plain"
echo

param=$(echo "$QUERY_STRING" | sed -n 's/^.*param=\([^&]*\).*$/\1/p')    # read value of "var1"
param_Dec=$(echo -e $(echo "$param" | sed 's/+/ /g;s/%\(..\)/\\x\1/g;'))    # html decode

cat /tmp/$param_Dec 
