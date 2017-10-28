"""Used to Display content to the screen."""
class Display:
    """class for displaying content to screen."""

    def __init__(self, is_verbose = False):
        """Constructor."""
        self._is_verbose = is_verbose

    def print_info(self, message):
        """Informational. Display if isVerbose is false."""
        if self._is_verbose:
            print ''.join(['Info: ', message])

    def print_warning(self, message):
        """Warning. Diplay is isVerbose is false."""
        if self._is_verbose:
            print ''.join(['Warning: ',  message])

    def print_error(self, message):
        """Error. Always displays."""
        print ''.join(['Error: ',  message])

    def print_fencers_to_screen(self, fencers):
        print 'swapping in the following entries'
        print 'Competitor List'

        for i in range(0, len(fencers)):
            self._print_fencer_row(fencers[i])
        print ''

    def print_pools_to_screen(self, pools):
        """.Display Pool to screen"""

        print 'Pool List'
        for i in range(0, len(pools)):
            fencers = sorted(pools[i].fencers, key = lambda f:f.numeric_skill_level, reverse=True)
            print ''.join(['--)------- ', pools[i].name, ' -------(--', '(', str(len(fencers)), ')'])

            for j in range(0, len(fencers)):
                self._print_fencer_row(fencers[j])
            print ' '

    def _print_fencer_row(self, fencer):
        print('{:15s}{:20s}{:25s}{:5s}{}'.format(fencer.first_name, fencer.last_name, fencer.print_friendly_club, fencer.skill_grade, fencer.skill_year))
