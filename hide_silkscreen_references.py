# -*- coding: utf-8 -*-
#
#  hide_silkscreen_references.py
#
#  Copyright 2022 Simon Hobbs <simon.hobbs@maskset.net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

from __future__ import print_function
import pcbnew
import wx
import os
from . import Dialog

class DialogEx(Dialog.Dialog):

    def onDeleteClick(self, event):
        return self.EndModal(wx.ID_DELETE)

def SetReferenceVisibility(visible=False, ignore_locked=True):
    for part in pcbnew.GetBoard().Footprints():
        if not part.IsLocked() and ignore_locked:
            ref = part.Reference()
            ref.SetVisible(visible)

class SetReferenceVisibilityAction(pcbnew.ActionPlugin):

    def defaults(self):
        self.name = "Set Reference Visibility"
        self.category = "Modify PCB"
        self.description = "Set reference visibility for all not locked parts"
        self.icon_file_name = None#os.path.join(os.path.dirname(__file__), "./stitching-vias.png")
        self.show_toolbar_button = True

    def Run(self):
        a = DialogEx(None)
        modal_result = a.ShowModal()
        print(modal_result)
        if modal_result == wx.ID_OK:
            try:
                SetReferenceVisibility(visible=a.SetVisible.IsChecked(), ignore_locked=a.IgnoreLocked.IsChecked())
            except Exception:
                wx.MessageDialog(None, "Invalid parameter")
        else:
            print("Cancel")
        a.Destroy()

SetReferenceVisibilityAction().register()
