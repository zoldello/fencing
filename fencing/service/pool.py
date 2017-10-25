"""Class for pool."""
import operator

from service.display import Display
from model.pool import Pool as PoolModel

class Pool:
    """Pool for divvying."""

    def __init__(self, fencersModel, isQuiet = False):
        """Initialize."""
        self._fencers = fencersModel
        self._fencersCount = 0
        self._display = Display(isQuiet)

        if self._fencers:
            self._fencersCount = len(fencersModel)

    def _getFencerDivvyCount(self):
        """Rules are that pools should consist of.
            mix of 6 and 7 fencers OR
            mix of 7 and 8 fencers OR
            mix of 5 and 6 fencers OR
            In this desending priority.
        """
        if not self._fencers or self._fencersCount == 0:
            _display.print_error("There are no fencers to divvy")
            return None

        for baseNumber in [6,7]:
            lengthDivision = self._fencersCount / baseNumber
            lengthModulus = self._fencersCount % baseNumber

            if (lengthDivision <= lengthModulus):
                return baseNumber

        return 5 # default

    def _createPools(self):
        """Create new teams."""
        pools = []
        poolSize = self._fencersCount / self._getFencerDivvyCount()

        if poolSize == None:
            self._display.print_error('Cannot get team size. Cannot proceed')
            return None

        for i in range(0, poolSize):
            name = ''.join(["Team", str(i + 1)])
            pool = Pool(name)
            pools.append(pool)

        return pools

    def _divvyFencersByClub(self):
        if not self._fencers:
            return None

        clubs = {}

        for fencer in self._fencers:
            club = fencer.club

            if not club in clubs:
                clubs[club] = []

            clubs[club].append(fencer)

        return clubs

    def _getPoolsSortedBySkill(self):
        clubs = self._divvyFencersByClub()
        sortedClubs = {} # sorted by skills

        for club, fencers in clubs.items():
            sortedClubs[club] =  sorted(fencers, key = lambda f:f.numericSkillLevel, reverse=True)

        return sortedClubs

    def getPools(self):
        """Get teams."""
        poolFencersCount = self._getFencerDivvyCount()
        remainderFencersToDivvy = self._fencersCount % poolFencersCount
        sortedClubs = self._getPoolsSortedBySkill()
        pools = self._createPools()

        maxClubFencersCount = max((len(fencers)) for club, fencers in sortedClubs.items())

        serpentineFencerGrouping = []

        for i in range(0, maxClubFencersCount):
            for club, fencers in sortedClubs.items():
                fencersCount = len(fencers)

                if i > (fencersCount - 1):
                    continue

                serpentineFencerGrouping.append(fencers[i])

        pools = []
        fencersSet = []

        for i in range(0, self._fencersCount, poolFencersCount):
            poolName = ''.join(['Pool#', str(i)])
            poolModel = PoolModel(poolName)
            for j in range(i, (i + poolFencersCount - 1)):
                poolModel.fencers.append(serpentineFencerGrouping[j])

            pools.append(poolModel)

        return pools
