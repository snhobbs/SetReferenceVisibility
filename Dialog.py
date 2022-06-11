# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-231-gdf7791bf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Dialog
###########################################################################

class Dialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 213,133 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer1.SetMinSize( wx.Size( 1,1 ) )
		self.IgnoreLocked = wx.CheckBox( self, wx.ID_ANY, u"Ignore Locked", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.IgnoreLocked.SetValue(True)
		bSizer1.Add( self.IgnoreLocked, 1, wx.ALL|wx.EXPAND, 5 )

		self.SetVisible = wx.CheckBox( self, wx.ID_ANY, u"Visible", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.SetVisible, 1, wx.ALL|wx.EXPAND, 5 )

		self.run_button = wx.Button( self, wx.ID_OK, u"run", wx.Point( 0,0 ), wx.DefaultSize, 0 )
		bSizer1.Add( self.run_button, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.run_button.Bind( wx.EVT_BUTTON, self.run_buttonOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def run_buttonOnButtonClick( self, event ):
		event.Skip()


