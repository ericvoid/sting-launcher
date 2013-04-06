def rounded_rectangle(cr, x, y, w, h, r=20):
    # This is just one of the samples from 
    # http://www.cairographics.org/cookbook/roundedrectangles/
    #   A****BQ
    #  H      C
    #  *      *
    #  G      D
    #   F****E

    cr.move_to(x+r,y)                      # Move to A
    cr.line_to(x+w-r,y)                    # Straight line to B
    cr.curve_to(x+w,y,x+w,y,x+w,y+r)       # Curve to C, Control points are both at Q
    cr.line_to(x+w,y+h-r)                  # Move to D
    cr.curve_to(x+w,y+h,x+w,y+h,x+w-r,y+h) # Curve to E
    cr.line_to(x+r,y+h)                    # Line to F
    cr.curve_to(x,y+h,x,y+h,x,y+h-r)       # Curve to G
    cr.line_to(x,y+r)                      # Line to H
    cr.curve_to(x,y,x,y,x+r,y)             # Curve to A


def setTransparency(win):
	win.set_decorated(False)

	# Makes the window paintable, so we can draw directly on it
	win.set_app_paintable(True)
	# win.set_size_request(100, 100)
	win.set_size_request(5, 5)
	# win.set_default_size(5, 5)

	# This sets the windows colormap, so it supports transparency.
	# This will only work if the wm support alpha channel
	screen = win.get_screen()
	rgba = screen.get_rgba_colormap()
	win.set_colormap(rgba)
