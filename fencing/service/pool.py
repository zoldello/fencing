"""Class for pool."""
import operator
import collections
import math

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
        fencer_divvy_count = self._get_fencer_divvy_count()
        sorted_by_skill = sorted(self._fencers, key=lambda f: (f.numeric_skill_level, f.last_name), reverse=True)
        pool_count = math.floor(self._fencers_count / fencer_divvy_count)
        pools = []

        for i in range(0,pool_count):
            pool_name = ''.join(['Pool #', str(i + 1)])
            pool_model = Pool_Model(pool_name)
            pools.append(pool_model)

        poolIndex = 0
        poolIndex2 = 0

        for fencer in self._fencers:
            currentPool = pools[poolIndex]
            poolIndex2 = poolIndex

            while any(f.print_friendly_club == fencer.club for f in pools[poolIndex2].fencers):
                poolIndex2 = poolIndex2 + 1 if poolIndex2 + 1  < pool_count else 0

                if (poolIndex2 == poolIndex):
                    break

                if len(pools[poolIndex2].fencers) == fencer_divvy_count:
                    continue

            poolIndex = poolIndex2 if poolIndex == poolIndex2 else poolIndex

            pools[poolIndex].fencers.append(fencer)
            poolIndex = poolIndex + 1 if (poolIndex + 1) < pool_count else 0

        return pools
