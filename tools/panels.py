## -*- coding: utf-8 -*-
## Partly generated by wxGlade 0.6.3 on Mon Aug 15 00:07:56 2011
##
## Created       : Fri Dec 02 13:46:17 IST 2011
## Last Modified : Fri Dec 02 16:28:58 IST 2011
##
## Copyright (c) 2011 Sriram Karra <karra.etc@gmail.com>
## All Rights Reserved
##
## Licensed under GPLv3
## 

import wx, logging, traceback
from   threading     import Thread

import tools.state

# begin wxGlade: extracode
# end wxGlade

class SyncPanel(wx.Panel):
    sync_dirs = [tools.state.SYNC_2_WAY,
                 tools.state.SYNC_1_WAY_O2G,
                 tools.state.SYNC_1_WAY_G2O]
    
    def __init__(self, gout, *args, **kwds):
        self.gout = gout

        # begin wxGlade: SyncPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.lblUsername = wx.StaticText(self, -1, "Username")
        self.txtUsername = wx.TextCtrl(self, -1, "")
        self.lblPass = wx.StaticText(self, -1, "Password")
        self.txtPass = wx.TextCtrl(self, -1, "", style=wx.TE_PASSWORD)
        self.lblGmGrp = wx.StaticText(self, -1, "Gmail Group")
        self.txtGmGrp = wx.TextCtrl(self, -1, "", style = wx.TE_READONLY)
#        self.chkContacts = wx.CheckBox(self, -1, "Contacts")
#        self.chkCal = wx.CheckBox(self, -1, "Calendar")
#        self.chkTasks = wx.CheckBox(self, -1, "Tasks")
        self.rdoSyncdir = wx.RadioBox(self, -1, "Sync Direction",
                                      choices=self.sync_dirs,
                                      majorDimension=0, style=wx.RA_SPECIFY_ROWS)
#        self.btnAdv = wx.Button(self, -1, "Advanced")
        self.btnClear = wx.Button(self, -1, "Clear Sync State")
        self.btnSync = wx.Button(self, -1, "Sync")
        self.btnDryRun = wx.Button(self, -1, "Dry Run")

        self.__set_properties()
        self.__do_layout()

#        self.Bind(wx.EVT_BUTTON, self.Adv, self.btnAdv)
        self.Bind(wx.EVT_BUTTON, self.Clear, self.btnClear)
        self.Bind(wx.EVT_BUTTON, self.do_sync, self.btnSync)
        self.Bind(wx.EVT_BUTTON, self.dry_run, self.btnDryRun)
        # end wxGlade
        self.SetSize((425,225))

    def __set_properties(self):
        # begin wxGlade: SyncPanel.__set_properties
        self.rdoSyncdir.SetSelection(0)
        # end wxGlade
        self.txtGmGrp.SetValue(self.gout.config.get_gn())

    def __do_layout(self):
        # begin wxGlade: SyncPanel.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
#        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(3, 2, 5, 5)
        grid_sizer_1.Add(self.lblUsername, 0, 0, 0)
        grid_sizer_1.Add(self.txtUsername, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.lblPass, 0, 0, 0)
        grid_sizer_1.Add(self.txtPass, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.lblGmGrp, 0, 0, 0)
        grid_sizer_1.Add(self.txtGmGrp, 0, wx.EXPAND, 0)
        sizer_1.Add(grid_sizer_1, 0, wx.ALL|wx.EXPAND, 5)

        # For now we only support synching of Contacts. We will
        # eventually allow support for tasks as well.

#        sizer_3.Add(self.chkContacts, 0, wx.ALL, 3)
#        sizer_3.Add(self.chkCal, 0, wx.ALL, 3)
#        sizer_3.Add(self.chkTasks, 0, wx.ALL, 3)
#        sizer_2.Add(sizer_3, 1, wx.ALL|wx.EXPAND, 5)

        sizer_2.Add(self.rdoSyncdir, 1, wx.ALL, 5)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
#        sizer_4.Add(self.btnAdv, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 0)
        sizer_4.Add(self.btnClear, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 0)
        sizer_4.Add(self.btnSync, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 0)
        sizer_4.Add(self.btnDryRun, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 0)
        sizer_1.Add(sizer_4, 1, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        # end wxGlade

#    def Adv(self, event): # wxGlade: SyncPanel.<event_handler>
#        self.Hide()
#        self.Parent.advpanel.Show()

    def Clear (self, event): # wxGlade: SyncPanel.<event_handler>
        self.Hide()
        self.gout.reset(self.txtUsername.GetValue(),
                        self.txtPass.GetValue(),
                        self.sync_dirs[self.rdoSyncdir.GetSelection()])

#        self.Parent.prgpanel.Show()
        self.Parent.syncpanel.Show()

    def dry_run (self, event):
        self.Hide()

        # Should ideally have a message box pop up to give details of
        # the error
        self.gout.dry_run(self.txtUsername.GetValue(),
                          self.txtPass.GetValue(),
                          self.sync_dirs[self.rdoSyncdir.GetSelection()])

        self.Parent.syncpanel.Show()

    def do_sync (self, event): # wxGlade: SyncPanel.<event_handler>
        self.Hide()

        # Should ideally have a message box pop up to give details of
        # the error
        self.gout.do_sync(self.txtUsername.GetValue(),
                          self.txtPass.GetValue(),
                          self.sync_dirs[self.rdoSyncdir.GetSelection()])

#        self.Parent.prgpanel.Show()
        self.Parent.syncpanel.Show()

# end of class SyncPanel


class ProgressPanel(wx.Panel):
    def __init__(self, gout, *args, **kwds):
        self.gout = gout

        # begin wxGlade: ProgressPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.txtProgress = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.btnOK = wx.Button(self, -1, "OK")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.PrgOK, self.btnOK)
        # end wxGlade
        self.SetSize((425,225))

    def __set_properties(self):
        # begin wxGlade: ProgressPanel.__set_properties
        self.Hide()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ProgressPanel.__do_layout
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_6.Add(self.txtProgress, 1, wx.ALL|wx.EXPAND, 5)
        sizer_6.Add(self.btnOK, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        self.SetSizer(sizer_6)
        sizer_6.Fit(self)
        # end wxGlade

    def PrgOK(self, event): # wxGlade: ProgressPanel.<event_handler>
        self.txtProgress.Value = ""
        self.Hide()
        self.Parent.syncpanel.Show()

# end of class ProgressPanel

## The Advanced panel might allow more advanced options such as choosing
## an Outlook profile other than the default profile, selecting one or
## more non-default message stores in the selected profile, etc. Such
## features are not currently supported. If and when they are, we can
## use the advanced panel customize such features.

#lass AdvPanel(wx.Panel):
#   def __init__(self, gout, *args, **kwds):
#       self.gout = gout        
#
#       # begin wxGlade: AdvPanel.__init__
#       kwds["style"] = wx.TAB_TRAVERSAL
#       wx.Panel.__init__(self, *args, **kwds)
#       self.lblProfile_copy = wx.StaticText(self, -1, "Outlook Profile")
#       self.cboProfile = wx.ComboBox(self, -1, choices=["Outlook Profile"], style=wx.CB_DROPDOWN)
#       self.lblStore = wx.StaticText(self, -1, "Store")
#       self.cboStore = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
#       self.lblLogLoc = wx.StaticText(self, -1, "Log File Location")
#       self.txtLogLoc = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
#       self.btnSelFolder = wx.Button(self, -1, "...")
#       self.lblNone = wx.StaticText(self, -1, "")
#       self.btnAdvOk = wx.Button(self, -1, "OK")
#
#       self.__set_properties()
#       self.__do_layout()
#
#       self.Bind(wx.EVT_BUTTON, self.SelFolder, self.btnSelFolder)
#       self.Bind(wx.EVT_BUTTON, self.AdvOk, self.btnAdvOk)
#       # end wxGlade
#       self.SetSize((425,225))
#       
#   def __set_properties(self):
#       # begin wxGlade: AdvPanel.__set_properties
#       self.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DFACE))
#       self.Hide()
#       self.cboProfile.SetMinSize((175, 21))
#       self.cboProfile.SetSelection(-1)
#       self.cboStore.SetMinSize((175, 21))
#       self.txtLogLoc.SetMinSize((150, 25))
#       self.btnSelFolder.SetMinSize((25, 25))
#       # end wxGlade
#       
#       
#   def __do_layout(self):
#       
#       # begin wxGlade: AdvPanel.__do_layout
#       grid_sizer_2 = wx.GridSizer(4, 2, 10, 10)
#       sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
#       grid_sizer_2.Add(self.lblProfile_copy, 0, wx.ALL, 10)
#       grid_sizer_2.Add(self.cboProfile, 0, wx.ALL, 10)
#       grid_sizer_2.Add(self.lblStore, 0, wx.ALL, 10)
#       grid_sizer_2.Add(self.cboStore, 0, wx.LEFT|wx.RIGHT, 10)
#       grid_sizer_2.Add(self.lblLogLoc, 0, wx.ALL, 10)
#       sizer_5.Add(self.txtLogLoc, 1, wx.LEFT, 10)
#       sizer_5.Add(self.btnSelFolder, 0, wx.RIGHT, 10)
#       grid_sizer_2.Add(sizer_5, 1, wx.EXPAND, 0)
#       grid_sizer_2.Add(self.lblNone, 0, 0, 0)
#       grid_sizer_2.Add(self.btnAdvOk, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 10)
#       self.SetSizer(grid_sizer_2)
#       grid_sizer_2.Fit(self)
#       # end wxGlade
#
#   def AdvOk(self, event): # wxGlade: AdvPanel.<event_handler>
#       self.Hide()
#       self.Parent.syncpanel.Show()
#
#   def SelFolder(self, event): # wxGlade: AdvPanel.<event_handler>
#       logloc = wx.DirDialog(None)
#       if logloc.ShowModal()==wx.ID_OK:
#           self.txtLogLoc.Value = logloc.GetPath()
#       logloc.Destroy()

# end of class AdvPanel


class SyncUI(wx.Frame):
    def __init__(self, gout, *args, **kwds):
        self.gout = gout

        # begin wxGlade: Sync.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
                
        self.syncpanel = SyncPanel(gout, self)
#        self.advpanel = AdvPanel(gout, self)
        self.prgpanel = ProgressPanel(gout, self)

    def __set_properties(self):
        # begin wxGlade: Sync.__set_properties
        self.SetTitle("Google Sync")
        self.SetSize((450, 260))
        self.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DFACE))
        # end wxGlade

    def __do_layout(self):        
        # begin wxGlade: Sync.__do_layout
        self.Layout()
        # end wxGlade

class Panels:
    def __init__ (self, gout):
        self.gout = gout
        self.app  = wx.PySimpleApp(0)

        wx.InitAllImageHandlers()

        self.fraSync = SyncUI(self.gout, None, -1, "")
        self.app.SetTopWindow(self.fraSync)

    def run (self):
        self.fraSync.Show()
        self.app.MainLoop()

# end of class Sync