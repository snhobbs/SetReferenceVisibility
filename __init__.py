# -*- coding: utf-8 -*-
# Two way of installation of this plugin:
#  - Copy or link this directory to KiCad plugin directory (~/.kicad_plugin/hide_silkscreen_references/)
#  - Copy files to ~/.kicad_plugin except __init__.py...
from __future__ import print_function
import pprint
import traceback
import sys

print("Starting plugin hide_silkscreen_references")
try:
    from .hide_silkscreen_references import *
except Exception as e:
    traceback.print_exc(file=sys.stdout)
    pprint.pprint(e)
