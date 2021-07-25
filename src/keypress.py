import urwid

def show_or_exit(key):
    if key in 'qQ':
        raise urwid.ExitMainLoop()
    txt.set_text(repr(key))

txt = urwid.Text('Hello World')
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()
