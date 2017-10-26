"""class for fencer model."""
import uuid

class Fencer:
    """Fencer."""

    def __init__(self, fencer):
        """Initialize."""
        self._faux_for_clubless = ''.join(['Club_', str(uuid.uuid4())])
        self._last_name = (fencer[0] or "").strip()
        self._first_name = (fencer[1] or "").strip()
        self._club = (fencer[2] or self._faux_for_clubless).strip()
        self._skill_level = (fencer[3] or "").strip()

        self._numeric_skill_level = self._get_numeric_skill()

    @property
    def last_name(self):
        """Last name."""
        return self._last_name

    @property
    def first_name(self):
        """First name."""
        return self._first_name

    @property
    def club(self):
        """Club."""
        return self._club

    @property
    def skill_level(self):
        """Skill level."""
        return self._skill_level

    @property
    def numeric_skill_level(self):
        """Numeric Skill level."""
        return self._numeric_skill_level

    def _get_numeric_skill(self):
        """Convert the fencer's skill to a numeric value. It is useful for things like sorting."""
        skill_letter = self._skill_level[0].upper()
        year_letter = self._skill_level[1:3]

        year = int(year_letter)

        # This converts the skill to a value, where A > B > C ... > Z. The
        # formular was choosen by arbituary, while trying to fine one that satisifies the skill-formular
        best_skill_grade_offset = ord(skill_letter) - 65
        numeric_skill_level = 1000 + ((10 - best_skill_grade_offset) * 1000) + year

        return numeric_skill_level
