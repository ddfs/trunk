#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ansible.utils.display import Display

import jsonpointer
import jsonpatch
from jsonmerge import merge

display = Display()

_nothing = object()

class FilterModule(object):
    def filters(self):
        return {
            'jsonpatch': self.jsonpatch,
            'jsonmerge': self.jsonmerge,
            'jsonpointer': self.jsonpointer,
        }

    def jsonpointer(self, doc, path, default=_nothing):
        return jsonpointer.resolve_pointer(doc, path, default)

    def jsonpatch(self, src, dst):
        patch = jsonpatch.make_patch(src, dst)
        return patch.apply(src)

    def jsonmerge(self, base, head, schema={}):
        display.warning('%s' % schema)
        return merge(base, head, schema)
