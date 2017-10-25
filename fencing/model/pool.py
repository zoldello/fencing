"""Pool class."""
import uuid

class Pool:
    """docstring for Team."""

    def __init__(self, name):
        """Initialize."""
        self._fauxForClubless = ''.join(['team_', str(uuid.uuid4())]) # used for fencers without club
        self._name = name or _fauxForClubless
        self._fencers = []


    @property
    def name(self):
        """name."""
        return self._name

    @property
    def fencers(self):
        """Getter for fencers."""
        return self._fencers

    #@fencers.setter
    #def fencers(self, fencer):
        #"""Setter for fencer."""
        #self._fencers.appen(fencers)
