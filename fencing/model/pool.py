"""Pool class."""


class Pool:
    """docstring for Pool."""

    def __init__(self, name):
        """Initialize."""
        self._name = name or ''
        self._fencers = []

    @property
    def name(self):
        """name."""
        return self._name

    @property
    def fencers(self):
        """Getter for fencers."""
        return self._fencers
