#!/usr/bin/env python2
# vim:fileencoding=utf-8
# License: GPLv3 Copyright: 2016, Kovid Goyal <kovid at kovidgoyal.net>

from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

from bypy.utils import simple_build


def main(args):
    simple_build('--disable-dependency-tracking --disable-static --enable-shared')


def filter_pkg(parts):
    return 'locale' in parts
