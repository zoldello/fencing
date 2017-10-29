"""Class for pool."""
import operator
import collections

from service.display import Display
from model.pool import Pool as Pool_Model


class Pool:
    """Pool for divvying."""

    def __init__(self, fencers_model, is_verbose=False):
        """Initialize."""
        self._fencers = fencers_model
        self._fencers_count = 0
        self._display = Display(is_verbose)

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

        for base_number in [6, 7]:
            division = self._fencers_count / base_number
            modulus = self._fencers_count % base_number

            if modulus == 0 or modulus == 1:
                return base_number

        return 5  # default

    def _divvy_fencers_by_club(self):
        """Group fencers by club."""
        if not self._fencers:
            return None

        clubs = collections.OrderedDict()

        for fencer in self._fencers:
            club = fencer.club

            if club not in clubs:
                clubs[club] = []

            clubs[club].append(fencer)

        return clubs

    def _get_pools_sorted_by_skill(self):
        clubs = self._divvy_fencers_by_club()
        sorted_clubs = collections.OrderedDict()  # sorted by skills

        for club, fencers in clubs.items():
            sorted_clubs[club] = sorted(fencers, key=lambda f: f.numeric_skill_level, reverse=True)

        return sorted_clubs

    def get_pools(self):
        """Get teams."""
        fencers_divvy_count = self._get_fencer_divvy_count()
        sorted_clubs = self._get_pools_sorted_by_skill()
        max_fencers_club_count = max((len(fencers)) for club, fencers in sorted_clubs.items())
        pool_count = self._fencers_count / fencers_divvy_count

        serpentine_fencers_grouping = []

        isReverse = False
        while any(fencers != [] for fencers in sorted_clubs.values()):
            temp_fencers = []
            for fencers in sorted_clubs.values():
                if not fencers:
                    continue

                temp_fencers.append(fencers.pop(0))

            isReverse = not isReverse
            serpentine_fencers_grouping.extend(sorted(temp_fencers, key=lambda f: f.numeric_skill_level, reverse=isReverse))

        pools = []

        for i in range(0, int(pool_count)):
            pool_name = ''.join(['Pool #', str(i + 1)])
            pool_model = Pool_Model(pool_name)
            pools.append(pool_model)

        for i in range(0, len(serpentine_fencers_grouping)):
            index = int(i % pool_count)

            pools[index].fencers.append(serpentine_fencers_grouping[i])

        return pools
