#!/bin/bash

# Initial setup on Ubuntu Hardy Heron
sudo adduser simplesite --home /home/simplesite

# Example commands
sudo -u simplesite mkdir /home/simplesite/download
cd /home/simplesite/download
sudo -u simplesite wget http://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.1.tar.gz
sudo -u simplesite tar zxfv virtualenv-1.1.tar.gz
sudo -u simplesite cp virtualenv-1.1/virtualenv.py ./

