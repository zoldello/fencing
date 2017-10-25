"""Used to Display content to the screen."""
class Display:
    """class for displaying content to screen."""

    def __init__(self, isQuiet = False):
        """Constructor."""
        self.isQuiet = isQuiet

    def print_info(self, message):
        """Informational. Display if isQuiet is false."""
        if not self.isQuiet:
            print ''.join(['Info', message])

    def print_warning(self, message):
        """Warning. Diplay is isQuiet is false."""
        if not self.isQuiet:
            print ''.join(['Warning: ',  message])

    def print_error(self, message):
        """Error. Always displays."""
        print ''.join(['Error: ',  message])

    def print_pools_to_screen(self, pools):
        """.Display Pool to screen"""
        print ' '
        
        for i in range(0, len(pools)):
            print pools[i].name

            fencers = pools[i].fencers
            for j in range(0, len(fencers)):
                fencer = fencers[j]
                print ''.join([fencer.lastName, ', ', fencer.firstName, ', ', fencer.club, ', ', fencer.skillLevel])

            print ' '
