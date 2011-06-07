'''
Module: orderedmapping.py
Version: 1.0

Author:
   Taro Ogawa (tso@users.sourceforge.org)
   
Copyright:
    Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.

Licence:
    This module is distributed under the Lesser General Public Licence.
    http://www.opensource.org/licenses/lgpl-license.php
'''
from __future__ import generators
class OrderedMapping(dict):
    def __init__(self, *pairs):
        self.order = []
        for key, val in pairs:
            self[key] = val
            
    def __setitem__(self, key, val):
        if key not in self:
            self.order.append(key)
        super(OrderedMapping, self).__setitem__(key, val)

    def __iter__(self):
        for item in self.order:
            yield item

    def __repr__(self):
        out = ["%s: %s"%(repr(item), repr(self[item])) for item in self]
        out = ", ".join(out)
        return "{%s}"%out
