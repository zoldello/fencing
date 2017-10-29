"""class for fencer model."""
import uuid

from service.display import Display


class Fencer:
    """Fencer."""

    def __init__(self, fencer):
        """Initialize."""
        display = Display(False)

        if not fencer:
            display.print_warning('Fencer is falsey. Cannot proceed')
            return

        self._faux_for_clubless = ''.join(['Club_', str(uuid.uuid4())])
        self._last_name = (fencer[0] or "").strip()
        self._first_name = (fencer[1] or "").strip()
        self._club = (fencer[2] or self._faux_for_clubless).strip()
        self._skill_level = (fencer[3] or "").strip().upper()
        self._skill_grade = self._skill_level[0]
        self._skill_year = self._skill_level[1:3]

        self._print_friendly_club = self._club if self._club != self._faux_for_clubless else ''
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

    @property
    def skill_year(self):
        """Skill year."""
        return self._skill_year

    @property
    def skill_grade(self):
        """Skill grade."""
        return self._skill_grade

    @property
    def print_friendly_club(self):
        """print-friendly club for clubless fencers."""
        return self._print_friendly_club

    def _get_numeric_skill(self):
        """Convert the fencer's skill to a numeric value. It is useful for things like sorting."""
        if self._skill_level[0] == 'U':
            return 0

        skill_grade = self._skill_level[0]
        year_letters = self._skill_level[1:3]

        year = int(year_letters)

        # This converts the skill to a value, where A > B > C > D > E. The
        # formular was choosen by arbituary, while trying to fine one
        # that satisifies the skill-formular
        best_skill_grade_offset = ord(skill_grade) - 65
        numeric_skill_level = 1000
        + ((10 - best_skill_grade_offset) * 1000)
        + year

        return numeric_skill_level
