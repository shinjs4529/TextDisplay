#!/usr/bin/env python
#-*- coding:utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Pango

class RealtimeDisplay(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Real-time Display")
        self.set_default_size(300, 80)

        self.label = Gtk.Label(label="Initial Text", xalign=0)
        self.label.modify_font(Pango.FontDescription("bold 14"))  # Adjust the font size here
        self.label.set_xalign(0.5)
        self.add(self.label)

        # Replace this function with your logic to update the text
        GLib.timeout_add_seconds(1, self.update_text)

    def update_text(self):
        # Replace this line with your logic to update the text dynamically
        new_text = "Updated Text"
        self.label.set_label(new_text)

        # Hide the window if the text is empty
        if not new_text:
            self.hide()
        else:
            self.show_all()

        return True

win = RealtimeDisplay()
win.set_decorated(False)  # Remove window decorations
win.set_position(Gtk.WindowPosition.CENTER)
win.show_all()

Gtk.main()
