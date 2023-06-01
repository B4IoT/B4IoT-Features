#!/bin/bash

echo "Content-type:text/plain"
echo

param=$(echo "$QUERY_STRING" | sed -n 's/^.*param=\([^&]*\).*$/\1/p')    # read value of "var1"
param_Dec=$(echo -e $(echo "$param" | sed 's/+/ /g;s/%\(..\)/\\x\1/g;'))    # html decode


getopt_simple()
{
    until [ -z "$1" ]
    do
      if [ ${1:0:2} = '--' ]
      then
          tmp=${1:2}	  # Strip off leading '--' . . .
	  parameter=${tmp%%=*}     # Extract name.
          value=${tmp##*=}         # Extract value.
          eval $parameter=$value
      fi
      shift
    done
}

target=/tmp

# Pass all options to getopt_simple().
getopt_simple "$param_Dec"

# list files to clean
echo "listing files in $target"
find "$target" -mtime 1

