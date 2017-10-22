"""class for fencer model."""
class Fencer:
    """Fencer."""

    def __init__(self, fencer):
        """Initialize."""
        self.lastName = fencer[0] or ""
        self.firstName = fencer[1] or ""
        self.team = fencer[2] or ""
        self.skillLevel = fencer[3] or ""

    @property
    def lastName(self):
        """Last name."""
        return self.lastName

    @property
    def firstName(self):
        """First name."""
        return self.firsName

    @property
    def team(self):
        """Team."""
        return self.team

    @property
    def skillLevel(self):
        """Skill level."""
        return self.skillLevel
