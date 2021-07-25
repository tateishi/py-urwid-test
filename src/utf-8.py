#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urwid

class MyEdit(urwid.Edit):
    def keypress(self, size, key):
        if key != 'enter':
            return super().keypress(size, key)
        else:
            raise urwid.ExitMainLoop()


def main():
    edit = MyEdit('お名前は？:')
    loop = urwid.MainLoop(urwid.Filler(edit))
    loop.run()


if __name__ == '__main__':
    main()
