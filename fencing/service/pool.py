"""Class for pool."""
import operator

from service.display import Display
from model.pool import Pool as Pool_Model

class Pool:
    """Pool for divvying."""

    def __init__(self, fencers_model, is_quiet = False):
        """Initialize."""
        self._fencers = fencers_model
        self._fencers_count = 0
        self._display = Display(is_quiet)

        if self._fencers:
            self._fencers_count = len(self._fencers)

    def _get_fencer_divvy_count(self):
        """Rules are that pools should consist of.
            mix of 6 and 7 fencers OR
            mix of 7 and 8 fencers OR
            mix of 5 and 6 fencers OR
            In this desending priority.
        """
        if not self._fencers or self._fencers_count == 0:
            _display.print_error("There are no fencers to divvy")
            return None

        for base_number in [6,7]:
            length_division = self._fencers_count / base_number
            length_modulus = self._fencers_count % base_number

            if (length_division <= length_modulus):
                return base_number

        return 5 # default

    def _divvy_fencers_by_club(self):
        """Group fencers by club."""
        if not self._fencers:
            return None

        clubs = {}

        for fencer in self._fencers:
            club = fencer.club

            if not club in clubs:
                clubs[club] = []

            clubs[club].append(fencer)

        return clubs

    def _get_pools_sorted_by_skill(self):
        clubs = self._divvy_fencers_by_club()
        sorted_clubs = {} # sorted by skills

        for club, fencers in clubs.items():
            sorted_clubs[club] =  sorted(fencers, key = lambda f:f.numeric_skill_level, reverse=True)

        return sorted_clubs

    def get_pools(self):
        """Get teams."""
        pool_fencers_count = self._get_fencer_divvy_count()
        sorted_clubs = self._get_pools_sorted_by_skill()
        max_fencers_club_count = max((len(fencers)) for club, fencers in sorted_clubs.items())

        serpentine_fencers_grouping = []

        for i in range(0, max_fencers_club_count):
            for club, fencers in sorted_clubs.items():
                fencersCount = len(fencers)

                if i > (fencersCount - 1):
                    continue

                serpentine_fencers_grouping.append(fencers[i])

        pools = []
        club_id = 1

        for i in range(0, self._fencers_count, pool_fencers_count):
            pool_name = ''.join(['Pool #', str(club_id)])
            club_id = club_id + 1
            pool_model = Pool_Model(pool_name)
            for j in range(i, (i + pool_fencers_count - 1)):
                pool_model.fencers.append(serpentine_fencers_grouping[j])

            pools.append(pool_model)

        return pools
