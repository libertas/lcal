#! /usr/bin/env sh

cp -r ./ /opt/lcal
echo "python3 /opt/lcal/lcal.py" > /usr/local/bin/lcal
chmod +x /usr/local/bin/lcal
