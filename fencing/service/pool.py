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

    def get_pools(self):

        """Get pools of fencers."""
        fencer_divvy_count = self._get_fencer_divvy_count()
        sorted_by_skill = sorted(self._fencers, key=lambda f: (f.numeric_skill_level, f.last_name), reverse=True)
        pool_count = math.floor(self._fencers_count / fencer_divvy_count)
        pools = []

        # create pools
        for i in range(0,pool_count):
            pool_name = ''.join(['Pool #', str(i + 1)])
            pool_model = Pool_Model(pool_name)
            pools.append(pool_model)
            poolIndex = -1 # init value, lowest values afterwards is 0

        for fencer in self._fencers:
            isFencerAssigned = False
            poolIndex = poolIndex + 1 if poolIndex + 1 < pool_count else 0

            # assigning fencer to pool while avoiding club-teammates
            for i in range(0, pool_count):
                if not any(f.print_friendly_club == fencer.club for f in pools[poolIndex].fencers) and len(pools[poolIndex].fencers) < fencer_divvy_count:
                    pools[poolIndex].fencers.append(fencer)
                    isFencerAssigned = True
                    break
                poolIndex = poolIndex + 1 if poolIndex + 1 < pool_count else 0

            if isFencerAssigned:
                continue

            # fencer must have teammate in club, spread out the fencer-numer
            # so clubs have fencer-count equals to fencer_divvy_count
            for j in range(0, pool_count):
                if len(pools[poolIndex].fencers) < fencer_divvy_count:
                    pools[poolIndex].fencers.append(fencer)
                    isFencerAssigned = True
                    break;
                poolIndex = poolIndex + 1 if poolIndex + 1 < pool_count else 0

            if isFencerAssigned:
                continue

            # at least one club fencer-count will be greater than fencer_divvy_count;
            # biased so fencer appear in earlier printed clubs (why k inseatd of poolIndex used)
            for k in range(0, pool_count):
                if len(pools[k].fencers) < fencer_divvy_count + 1:
                    pools[k].fencers.append(fencer)
                    break;

        return pools
