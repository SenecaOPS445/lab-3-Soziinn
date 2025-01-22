#!/usr/bin/env python3
# Author ID: 133245233

import os

def free_space():
    output = os.popen("df -h | grep '/$' | awk '{print $4}'").read()
    return output.strip()
print(free_space())
