import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="This si the title")

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.button.connect("clicked", functions.onButton1Clicked)
        
        self.label = Gtk.Label(label="Hello World", angle=220, halign=Gtk.Align.END)
        
        self.add(self.label)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello World")


class functions():
	def onButton1Clicked(self):
		print("test")

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
