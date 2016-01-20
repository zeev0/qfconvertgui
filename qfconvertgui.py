#!/usr/bin/env python

from gi.repository import Gtk
import os

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="qfconvertergui")
        self.set_default_size(400,10)

        grid = Gtk.Grid()
        self.add(grid)

        qf_entry = self.qf_entry = Gtk.Entry()
        qf_entry.set_hexpand(True)
        qf_entry.set_placeholder_text("Path to qfconverter's root directory...")

        df_entry = self.df_entry = Gtk.Entry()
        df_entry.set_hexpand(True)
        df_entry.set_placeholder_text("Path to Dwarf Fortress' macros directory...")

        file_entry = self.file_entry = Gtk.Entry()
        file_entry.set_hexpand(True)
        file_entry.set_placeholder_text("Path to the csv/xls file...")

        infobox = self.infobox = Gtk.TextView(editable=False)
        infobox.set_vexpand(True)
        infobox.set_hexpand(True)

        qf_button = Button(qf_entry, label="Open")
        qf_button.connect('clicked', self.on_dir_open)

        df_button = Button(df_entry, label="Open")
        df_button.connect('clicked', self.on_dir_open)

        file_button = Button(file_entry, label="Open")
        file_button.connect('clicked', self.on_file_open)

        go_button = Gtk.Button(label="Go!")

        grid.attach(qf_button,  0,0,1,1)
        grid.attach(qf_entry,   1,0,1,1)
        grid.attach(df_button,  0,1,1,1)
        grid.attach(df_entry,   1,1,1,1)
        grid.attach(file_button,0,2,1,1)
        grid.attach(file_entry, 1,2,1,1)
        grid.attach(infobox,    0,3,2,1)
        

    def on_dir_open(self, widget):
        chooser = Gtk.FileChooserDialog("Please choose a directory", self,
                                        Gtk.FileChooserAction.SELECT_FOLDER,
                                        (Gtk.STOCK_CANCEL,
                                         Gtk.ResponseType.CANCEL,
                                         Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        response = chooser.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("Folder selected: " + chooser.get_filename())
            widget.friend.set_text(chooser.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        chooser.destroy()

    def on_file_open(self,widget):
        chooser = Gtk.FileChooserDialog("Please choose a directory", self,
                                        Gtk.FileChooserAction.OPEN,
                                        (Gtk.STOCK_CANCEL,
                                         Gtk.ResponseType.CANCEL,
                                         Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        response = chooser.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("Folder selected: " + chooser.get_filename())
            widget.friend.set_text(chooser.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        chooser.destroy()

    #TODO
    def on_go(self,widget):
        macros_dir = self.df_entry.get_text()
        qf_dir = self.qf_entry.get_text()
        filename = self.file_entry.get_text()



class Button(Gtk.Button):

    def __init__(self, friend, label=''):
        Gtk.Button.__init__(self,label)
        self.friend = friend
    
win = Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
