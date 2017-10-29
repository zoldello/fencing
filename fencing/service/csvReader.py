"""Read in file."""
import csv
import os

from service.display import Display


class CsvReader:
    """Reads in data from source."""

    def __init__(self, file, isVerbose=False):
        """constructor."""
        self._file = file
        self._absolute_path = os.path.abspath(file)
        self._display = Display(isVerbose)

    def _is_file_valid(self):
        """Check validity of file."""
        isValid = True

        if not self._file:
            self._display.print_error('File does not exist')
            isValid = False

        if not os.path.isfile(self._absolute_path):
            self._display.print_error('File does not exist. Name is: {0}'.format(self._absolute_path))
            isValid = False

        return isValid

    def read(self):
        """Read in csv file."""
        if not self._is_file_valid():
            return None

        self._display.print_info('Reading file: {0}'.format(self._file))
        content = []

        with open(self._absolute_path) as csvFile:
            reader = csv.reader(csvFile, delimiter=',')
            for row in reader:
                content.append(row)

        contentLength = len(content)

        if not (contentLength >= 12 and contentLength < 100):
            self._display.print_error('Fencers-count is outside range of 12 and 100. The count is: {0}'.format(contentLength))
            return None

        self._display.print_info('fencer #: {0}'.format(contentLength))

        return content
