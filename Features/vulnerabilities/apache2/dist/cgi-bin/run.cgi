#!/bin/bash

echo "Content-type:text/plain"
echo
Var1=$(echo "$QUERY_STRING" | sed -n 's/^.*test=\([^&]*\).*$/\1/p')    # read value of "var1"
Var1_Dec=$(echo -e $(echo "$Var1" | sed 's/+/ /g;s/%\(..\)/\\x\1/g;'))    # html decode

echo -e "HELLO WORLD\nYour URL path is ${Var1}"

