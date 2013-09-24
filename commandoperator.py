import gtk


class Operator:

    def __init__(self, widget, command_source):
        self.found_commands = []
        
        self.current_item = None
        self.current_item_id = 0
        self.search_text = ''

        self.widget = widget

        self.source = command_source


    def keypress(self, widget, event) :
        if event.keyval == gtk.keysyms.Escape :
            self.handleEscape()
            return
        
        if event.keyval == gtk.keysyms.Return :
            self.run_command()
            self.widget.quit()
            return

        self.processKey(event.keyval)


    def handleEscape(self):
        if self.search_text == '':
            self.widget.quit()
        else:
            self.found_commands = []
            self.current_item = None
            self.current_item_id = 0
            self.search_text = ''
            
            self.widget.resetText()
            self.widget.dothemagic()
    
    def handleBackSpace(self):
        if len(self.search_text) > 1:
            self.search_text = self.search_text[:-1]
        else:
            self.search_text = ''
            self.widget.resetText()
            self.widget.dothemagic()

    def clampCurrentItemId(self):
        if self.current_item_id < 0:
            self.current_item_id = 0
        elif self.current_item_id >= len(self.found_commands):
            self.current_item_id = len(self.found_commands) - 1


    def searchCommands(self):
        found = self.source.search(self.search_text)
        self.found_commands = sorted(found, key=lambda i: i.distance)


    def processKey(self, keyval):
        if keyval == gtk.keysyms.Up:
            self.current_item_id -= 1

        elif keyval == gtk.keysyms.Down:
            self.current_item_id += 1

        elif keyval == gtk.keysyms.BackSpace:
            self.handleBackSpace()
            self.searchCommands()

        elif keyval < 255:
            self.search_text += chr(keyval)
            self.searchCommands()

        if len(self.search_text) > 0:
            self.clampCurrentItemId()
            self.showCurrent()


    def showCurrent(self):
        if len(self.found_commands) < 1:
            self.widget.text = "not found"
            self.widget.matching_idx = []
            self.widget.dothemagic()
        
        else:
            self.current_item = self.found_commands[self.current_item_id]
            self.widget.text = self.current_item.name
            self.widget.matching_idx = self.current_item.matching_idx
            
            self.widget.dothemagic()


    def run_command(self):
        self.source.run(self.current_item)

