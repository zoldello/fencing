"""Read in file."""
import csv
import os
import collections

from service.display import Display


class Csv_Reader:
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
        read = collections.OrderedDict()

        with open(self._absolute_path) as csvFile:
            reader = csv.reader(csvFile, delimiter=',')
            for row in reader:
                read[str(int(reader.line_num))] = row

        readLength = len(read)

        if not (readLength >= 12 and readLength < 101):
            self._display.print_error('Fencers-count is outside range of 12 and 100. The count is: {0}'.format(contentLength))
            return None

        self._display.print_info('fencer #: {0}'.format(readLength))

        return read
