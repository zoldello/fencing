"""Read in file."""
import csv
import os

from service.display import Display

class DataReader:
    """Reads in data from source."""

    def __init__(self, file, isQuiet = False):
        """constructor."""
        self.file = file
        self.fileFullPath = os.path.abspath(file)
        self.display = Display(isQuiet)

    def isFileValid(self):
        """Check validity of file."""
        isValid = True

        if not self.file:
            self.display.print_error('File does not exist')
            isValid = False

        if not os.path.isfile(self.fileFullPath):
            self.display.print_error('File does not exist. File name is: {0}'.format(self.fileFullPath))
            isValid = False

        return isValid

    def csv(self):
        """Read in csv file."""
        if not self.isFileValid():
            return None

        self.display.print_info('Reading a file with name: {0}'.format(self.file))
        csvFileContent = []

        with open(self.fileFullPath) as csvFile:
            reader = csv.reader(csvFile, delimiter=',')
            for row in reader:
                csvFileContent.append(row)

        csvFileContentLength = len(csvFileContent)

        if not (csvFileContentLength >= 12 and csvFileContentLength < 100):
            self.display.print_error('The number of fencers is not with in the range of 12 and 100 (100 is inclusive.). The range you have is: {0}'.format(csvFileContentLength))
            return None

        self.display.print_info('Number of fencers: {0}'.format(csvFileContentLength))

        return csvFileContent
