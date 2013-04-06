#! /usr/bin/env python

import gtk
from gtk_moar import setTransparency

from aliases import Aliases

from commandoperator import Operator
from hud import Hud


def run(widget, operator, command_source):
    window = gtk.Window()

    canvas = widget(window)
    
    window.connect("delete_event", canvas.delete_event)
    window.connect("destroy", canvas.destroy)

    op = operator(canvas, command_source())
    window.connect("key-press-event", op.keypress)

    setTransparency(window)

    window.add(canvas)
    window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
    window.show_all()
    gtk.main()


if __name__ == '__main__':
    run(Hud, Operator, Aliases)