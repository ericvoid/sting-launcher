import gtk
import cairo
#import time

from math import trunc

from gtk_moar import rounded_rectangle
import common

class Hud(gtk.DrawingArea):
    config_name = '~/.config/sting/colors'

    def __init__(self, window):
        super(Hud, self).__init__()

        self.connect("expose_event", self.expose)
        
        self.thewindow = window
        self.widget = None
        
        self.matching_idx = []
        self.text = ''
        self.resetText()

        self.backgroundColor = (0.0, 0.0, 0.0, 0.66)
        self.foregroundColor = (0.4, 0.59, 0.83)
        self.highlightColor  = (1.0, 1.0, 1.0)

        self.readConfig()
    
    def readConfig(self):
        for name, value in common.readConfig(Hud.config_name):
            if name == 'background':
                self.backgroundColor = common.hex_to_rgba(value)
            elif name == 'foreground':
                self.foregroundColor = common.hex_to_rgb(value)
            elif name == 'highlight':
                self.highlightColor = common.hex_to_rgb(value)
            else :
                raise Exception('whoa')

    def resetText(self):
        t = "type it" # t = "The quick brown fox jumps over the lazy dog."
        
        self.matching_idx = []
        
        if self.text == t:
            return False
        
        self.text = t
        
        return True

    def expose(self, widget, event):
        self.widget = widget
        self.dothemagic()
        

    def dothemagic(self):
        cr = self.widget.window.cairo_create()
        
        self.thewindow.set_size_request(5, 5)

        # Sets the operator to clear which deletes everything below where an object is drawn
        cr.set_operator(cairo.OPERATOR_CLEAR)
        # Makes the mask fill the entire window
        cr.rectangle(0.0, 0.0, *self.widget.window.get_size())
        #time.sleep(1)
        # Deletes everything in the window (since the compositing operator is clear and mask fills the entire window
        cr.fill()
        # Set the compositing operator back to the default
        cr.set_operator(cairo.OPERATOR_OVER)

        rect = self.get_allocation()

        # you can use w and h to calculate relative positions which
        # also change dynamically if window gets resized
        w = rect.width
        h = rect.height
        
        rounded_rectangle(cr, 0, 0, w, h, 5)
        cr.set_source_rgba(*self.backgroundColor)
        cr.fill()
        
        nw, nh = self.printCharByChar(cr)
        
        self.thewindow.resize(trunc(round(nw)), trunc(round(nh)))
        

    def printCharByChar(self, cr):
        font_size = 42

        cr.select_font_face("Liberation Serif", cairo.FONT_SLANT_NORMAL)
        cr.set_font_size(font_size)

        x = 14
        y = font_size + 5
        total_width = 0
        for i, c in enumerate(self.text):
            
            if i in self.matching_idx:
                cr.set_source_rgb(*self.highlightColor)
            else:
                # cr.set_source_rgb(0.5, 0.5. 1.0)
                # rgb(102, 151, 214)
                cr.set_source_rgb(*self.foregroundColor)
                
            xbearing, ybearing, width, height, xadvance, yadvance = cr.text_extents(c)
            
            cr.move_to(x, y)
            cr.show_text(c)
            x += xadvance
            total_width += xadvance

        #print total_width + 31, font_size + 25, self.text
        return (total_width + 31, font_size + 25)
    
         
    def delete_event(self, widget, event, data=None):
        # print "delete_event ocurred"
        # print widget, event, data
        return False
                
    def destroy(self, widget, data=None):
        # print "destroying"
        # print widget, data
        gtk.main_quit()

    def quit(self):
        gtk.main_quit()