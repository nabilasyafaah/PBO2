# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"192410101100 NABILA SYAFA'AH SHOUFIA DALILLAH", pos = wx.DefaultPosition, size = wx.Size( 500,282 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"HELLO WX", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 48, 74, 90, 92, False, "Gill Sans MT" ) )
		self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		bSizer2.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrl9 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl9, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"NIM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_textCtrl10 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl10, 0, wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self.m_panel2, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		self.m_panel2.SetSizer( fgSizer1 )
		self.m_panel2.Layout()
		fgSizer1.Fit( self.m_panel2 )
		bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"New"+ u"\t" + u"CTRL+N", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem4 )
		
		self.m_menuItem5 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Save"+ u"\t" + u"CTRL+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem5 )
		
		self.m_menuItem6 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit"+ u"\t" + u"ALT+F4", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem6 )
		
		self.m_menubar1.Append( self.m_menu1, u"File" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Undo"+ u"\t" + u"CTRL+Z", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Redo"+ u"\t" + u"CTRL+Y", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem3 )
		
		self.m_menubar1.Append( self.m_menu2, u"Edit" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"About..."+ u"\t" + u"F1", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem1 )
		
		self.m_menubar1.Append( self.m_menu3, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_button1OnButtonClick( self, event ):
		event.Skip()
	

