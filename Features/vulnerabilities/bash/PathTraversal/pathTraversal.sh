#!/bin/bash
echo "Hello, what directory in the client section do you want to read?"
read path
echo "Here is the file: /home/client/$path "
cat "/home/client/$path"
