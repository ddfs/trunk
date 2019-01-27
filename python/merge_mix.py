#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from collections.abc import MutableMapping, MutableSequence
except ImportError:
    from collections import MutableMapping, MutableSequence

#
# merge all nodes in dict objects and combine list nodes
#
# x as base
# y as update
#
# takes x as schema when applying y to update
# do not allow changes in data type unless None
#
# feel free to replace with built-in copy, map, itertools etc as you like.
#

def f(x, y):
    rx = x
    ry = y
    xy = {}

    for k in rx:
        if k in ry and isinstance(rx[k], MutableMapping) and isinstance(ry[k], MutableMapping):
            xy[k] = f(rx[k], ry[k])
        elif k in ry and isinstance(rx[k], MutableSequence) and isinstance(ry[k], MutableSequence):
            xy[k] = ry[k] + rx[k]
        elif k not in ry and isinstance(rx[k], MutableMapping):
            xy[k] = f(x[k], {})
        elif k not in ry and isinstance(rx[k], MutableSequence):
            xy[k] = rx[k] if k not in xy else  xy[k] + rx[k]
        else:
            xy[k] = rx[k]

    for k in ry:
        if k in rx and isinstance(ry[k], MutableMapping) and isinstance(rx[k], MutableMapping):
            xy[k] = f(ry[k], rx[k])
        elif k in rx and isinstance(ry[k], MutableSequence) and isinstance(rx[k], MutableSequence):
            xy[k] = ry[k] + rx[k]
        elif k not in rx and isinstance(ry[k], MutableMapping):
            xy[k] = ry[k]
        elif k not in rx and isinstance(ry[k], MutableSequence):
            xy[k] = ry[k] if k not in xy else xy[k]  + ry[k]
        else:
            # for type check against base
            # override when value is none, fail if type is different
            if not isinstance(xy[k], type(ry[k])) and xy[k] is not None:
                raise Exception("types must match in x/y: { %s: %s }" % (k, ry[k]))
            xy[k] = ry[k]

    return xy

#
# sample data
#
base = {
    'a': {
        'b': [1, 2]
    },
    'b': {
        'b': []
    },
    'c': None
}

update = {
    'a': {
        'b': [3, 'a']
    },
    'b': {
        'a': {
            'a': 2
        },
        'b': [1, 2],
        'c': [123]
    },
    'c': {
        'a': [3, 4]
    }
}

print('---')
print('--- base')
print(base)
print('--- update')
print(update)
print('---')
print("--- update/base")
try:
    print f(update, base)
except Exception as e:
    print (e.message)
print("--- base/update")
try:
    print f(base, update)
except Exception as e:
    print (e.message)
print("---")
