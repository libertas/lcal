#! /usr/bin/env sh

cp -r ./ /opt/
echo "python3 /opt/lcal.py" > /usr/local/bin/lcal
chmod +x /usr/local/bin/lcal
