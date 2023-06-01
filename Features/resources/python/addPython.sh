#!/bin/bash
apk add python3 
wget  https://bootstrap.pypa.io/get-pip.py
# This damn subprocess.run corrupts pip 
# https://superuser.com/questions/1447168/python-pip-install-error-shlex-py
# https://github.com/xando/subprocess.run/issues/5
rm  -rf /usr/lib/python3.9/site-packages/subprocess.run*
python3 get-pip.py
rm get-pip.py
python3 -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org --upgrade pip
/usr/bin/pip config set global.trusted-host "pypi.org pypi.python.org files.pythonhosted.org"