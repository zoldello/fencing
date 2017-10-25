"""class for fencer model."""
class Fencer:
    """Fencer."""

    def __init__(self, fencer):
        """Initialize."""
        self._lastName = fencer[0] or ""
        self._firstName = fencer[1] or ""
        self._club = fencer[2] or ""
        self._skillLevel = fencer[3] or ""

        self._numericSkillLevel = self._getNumericSkill()

    @property
    def lastName(self):
        """Last name."""
        return self._lastName

    @property
    def firstName(self):
        """First name."""
        return self._firsName

    @property
    def club(self):
        """Club."""
        return self._club

    @property
    def skillLevel(self):
        """Skill level."""
        return self._skillLevel

    @property
    def numericSkillLevel(self):
        """Numeric Skill level."""
        return self._numericSkillLevel

    def _getNumericSkill(self):
        """This is a util that converts the skills to a numeric value. It is useful for things like sorting"""
        skill = self._skillLevel.strip()
        skillLetter = skill[0].upper()
        yearLetter = skill[1:3]

        year = int(yearLetter)

        # This converts the skill to a value, where A > B > C ... > Z. The
        # formular was choosen by arbituary, while trying to fine one that satisifies the skill-formular
        offsetFromBestSkill = ord(skillLetter) - 65
        numericSkillLevel = 1000 + ((10 - offsetFromBestSkill)* 1000) + year

        return numericSkillLevel
