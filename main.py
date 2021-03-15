import wx
import helloWxGUI

class subClass(helloWxGUI.MyFrame1):
    def __init__(self, parent):
        helloWxGUI.MyFrame1.__init__(self,parent)
        
    def m_button1OnButtonClick(self, event):
        print("Tersimpan!")

app = wx.App()
frame = subClass(parent=None)
frame.Show()
app.MainLoop()