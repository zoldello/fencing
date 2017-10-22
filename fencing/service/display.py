"""Used to Display content to the screen."""
class Display:
    """class for displaying content to screen."""
    
    def __init__(self, isQuiet = False):
        """Constructor."""
        self.isQuiet = isQuiet

    def print_info(self, message):
        """Informational. Display if isQuiet is false."""
        if not self.isQuiet:
            print 'Info: ' + message

    def print_warning(self, message):
        """Warning. Diplay is isQuiet is false."""
        if not self.isQuiet:
            print "Warning:" + message

    def print_error(self, message):
        """Error. Always displays."""
        print "Error:" + message
