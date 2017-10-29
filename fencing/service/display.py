"""Used to Display content to the screen."""
import operator


class Display:
    """class for displaying content to screen."""

    def __init__(self, is_verbose=False):
        """Constructor."""
        self._is_verbose = is_verbose

    def print_info(self, message):
        """Informational. Display if isVerbose is false."""
        if self._is_verbose:
            print(''.join(['Info: ', message]))

    def print_warning(self, message):
        """Warning. Diplay is isVerbose is false."""
        if self._is_verbose:
            print(''.join(['Warning: ',  message]))

    def print_error(self, message):
        """Error. Always displays."""
        print(''.join(['Error: ',  message]))

    def print_fencers_to_screen(self, fencers):
        """Print list of fencers to screen."""

        if not fencers:
            self.print_warning('Fencers to print to screen is empty')
            return

        print(''.join(['Competitor List', ' (', str(len(fencers)), ' ', 'fencers', ')']))

        for fencer in fencers:
            self._print_fencer_row(fencer)
        print('')

    def print_pools_to_screen(self, pools):
        """.Display Pool to screen."""
        print('Pool List')
        for i in range(0, len(pools)):
            fencers = sorted(pools[i].fencers, key=lambda f: f.numeric_skill_level, reverse=True)
            print(''.join(['--)------- ', pools[i].name, ' -------(--', '(', str(len(fencers)), ')']))

            for fencer in fencers:
                self._print_fencer_row(fencer)
            print(' ')

    def _print_fencer_row(self, fencer):
        print('{:15s}{:20s}{:25s}{:5s}{}'.format(fencer.first_name, fencer.last_name, fencer.print_friendly_club, fencer.skill_grade, fencer.skill_year))
