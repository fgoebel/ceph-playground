#!/usr/bin/python
import re

def cephfs_get_secret(a):
    pattern = re.compile(r"key = (.*)$")
    key = pattern.search(a)
    if key == None:
        return "NO KEY FOUND"
    else:
        return key.group(1)

class FilterModule(object):
    def filters(self):
        return {'cephfs_extract_secret': cephfs_get_secret }
