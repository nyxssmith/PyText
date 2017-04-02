import gi
import time
import threading

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

rotating = False

class MyWindow(Gtk.Window):
    label = Gtk.Label(label="Hello World", angle=220, halign=Gtk.Align.END)

    def __init__(self):
        Gtk.Window.__init__(self, title="This si the title")
        grid = Gtk.Grid()
        self.add(grid)
        global label

        button1 = Gtk.Button(label="Button 1")
        button2 = Gtk.Button(label="start rotation")
        button3 = Gtk.Button(label="stop rotation")
        button4 = Gtk.Button(label="rotate a bit")
        button5 = Gtk.Button(label="set angle to 29")
        button6 = Gtk.Button(label="print angle")
        blank = Gtk.Label(label="", angle=220, halign=Gtk.Align.END)
    

        grid.add(button1)
        grid.attach(button2, 1, 0, 2, 1)
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)
        
        button1.connect("clicked", functions.onButtonClicked,button1)

        button2.connect("clicked", functions.startRotation,self.label)

        button3.connect("clicked", functions.stopRotation)

        button4.connect("clicked", functions.rotateAngle,self.label)

        button5.connect("clicked", functions.setAngle,self.label,29)

        button6.connect("clicked", functions.getAngle,self.label)
        
        grid.attach(self.label,3,3,1,1)
        
        grid.attach(blank,4,4,2,2)
        
        #label.connect("clicked",functions.test)
    def getLabel(self):
	    return self.label



class functions():
	def test():
		print("test")
	
	def rotateAngle(self,widget):
		angle = widget.get_angle()
		widget.set_angle(angle+10)
		print("The angle of",widget,"is now",widget.get_angle())
		
	def getAngle(self,widget):
		print("The angle of",widget,"is ",widget.get_angle())
		
	def setAngle(self,widget,angle):
		widget.set_angle(angle)
		print("The angle of",widget,"is now",widget.get_angle())
	
		
	def startRotation(self,widget):
		print("starting rotation")
		global rotating
		rotating = True
		t1 = threading.Thread(target=otherThreadedObjects.rotate)
		# classifying as a daemon, so they will die when the main dies
		t1.daemon = True
		# begins, must come after daemon definition
		t1.start()

	def stopRotation(self):
		print("stopping rotation")
		global rotating
		rotating = False

	
	def onButtonClicked(self,widget):
		print("test")
		print(threading.currentThread())
		print(widget.get_label())

#for use of udp server only
class otherThreadedObjects():#IMPRTANT: do not use this to update other ui elements, it crashes the universe
	def rotate():
		
		#print(threading.currentThread())
		widget=MyWindow.getLabel(MyWindow)
		angle = widget.get_angle()
		widget.set_angle(angle+1)
		print(angle)
		while(rotating):
			print(threading.currentThread())
			time.sleep(.01)
			angle = widget.get_angle()
			widget.set_angle(angle+1)
		
		print(rotating)
		print(threading.currentThread())
	


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()		

mainThread = threading.Thread(target=Gtk.main())
# classifying as a daemon, so they will die when the main dies
mainThread.daemon = True
mainThread.name = "gui"
# begins, must come after daemon definition
mainThread.start()


