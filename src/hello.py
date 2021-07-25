import urwid

txt = urwid.Text('Hello World')
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill)
try:
    loop.run()
except:
    pass
