"""Used to Display content to the screen."""
class Display:
    """class for displaying content to screen."""

    def __init__(self, is_quiet = False):
        """Constructor."""
        self._is_quiet = is_quiet

    def print_info(self, message):
        """Informational. Display if isQuiet is false."""
        if not self._is_quiet:
            print ''.join(['Info', message])

    def print_warning(self, message):
        """Warning. Diplay is isQuiet is false."""
        if not self._is_quiet:
            print ''.join(['Warning: ',  message])

    def print_error(self, message):
        """Error. Always displays."""
        print ''.join(['Error: ',  message])

    def print_fencers_to_screen(self, fencers):
        print 'swapping in the following entries'
        print 'Competitor List'

        for i in range(0, len(fencers)):
            club = ''

            if (fencers[i].club == fencers[i].faux_club):
                club = ""
            else:
                club = fencers[i].club

            print ' '.join([fencers[i].first_name, fencers[i].last_name, club, fencers[i].skill_grade, fencers[i].skill_year])
        print ''

    def print_pools_to_screen(self, pools):
        """.Display Pool to screen"""

        print 'Pool List'
        for i in range(0, len(pools)):
            fencers = sorted(pools[i].fencers, key = lambda f:f.numeric_skill_level, reverse=True)
            print ''.join(['--)------- ', pools[i].name, ' -------(--', '(', str(len(fencers)), ')'])

            for j in range(0, len(fencers)):
                fencer =  fencers[j]
                print ' '.join([fencer.first_name, fencer.last_name, fencer.club, fencer.skill_level])

            print ' '
