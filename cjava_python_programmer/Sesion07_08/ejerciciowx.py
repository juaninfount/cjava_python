import wx

app = wx.App(False)
frame = wx.Frame(None,-1, 'wxPython Prueba')
panel = wx.Panel(frame,-1)
btn=wx.Button(panel,-1,"Clic me!")
frame.Show()
app.MainLoop()