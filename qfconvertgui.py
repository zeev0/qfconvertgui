#!/usr/bin/env python
#
# qfconvertergui.py
# -----------------
import os
from gi.repository import Gtk
from subprocess import Popen,PIPE

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="qfconvertergui")
        self.set_default_size(400,10)

        grid = Gtk.Grid()
        self.add(grid)

        qf_entry = self.qf_entry = Gtk.Entry()
        qf_entry.set_hexpand(True)
        qf_entry.set_placeholder_text("Path to qfconverter's root directory...")
        qf_entry.set_text(os.getcwd())

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
        go_button.connect('clicked', self.on_go)

        grid.attach(qf_button,  0,0,1,1)
        grid.attach(qf_entry,   1,0,1,1)
        grid.attach(df_button,  0,1,1,1)
        grid.attach(df_entry,   1,1,1,1)
        grid.attach(file_button,0,2,1,1)
        grid.attach(file_entry, 1,2,1,1)
        grid.attach(go_button,  0,3,2,1)
        grid.attach(infobox,    0,4,2,1)
        

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
            widget.friend.set_text(chooser.get_filename())
        chooser.destroy()


    def on_go(self,widget):
        macros_dir = self.df_entry.get_text() + '/'
        qf = self.qf_entry.get_text() + '/qfconvert.py'
        csv = self.file_entry.get_text()
        # what the fuck?
        macro_name = os.path.splitext(csv)[0].split('/')[::-1][0] + '.mak'
        subprocess = Popen(["python", qf, csv, macros_dir + macro_name],
                           stdout=PIPE, stderr=PIPE)
        output, err = subprocess.communicate()
        buf_txt = output + err
        if buf_txt == '':
            buf_txt = 'Success! Created macro file ' + macro_name
        print(output,err)
        buf = Gtk.TextBuffer()
        buf.set_text(buf_txt)
        self.infobox.set_buffer(buf)


class Button(Gtk.Button):

    def __init__(self, friend, label=''):
        Gtk.Button.__init__(self,label)
        self.friend = friend
    

def main():
    win = Window()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
    
if __name__ == "__main__":
    main()
