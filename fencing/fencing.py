"""Entry point to the application."""
import argparse

from service.display import Display
from service.dataReader import DataReader
from service.pool import Pool as PoolService
from model.pool import Pool as PoolModel
from model.fencer import Fencer

parser = argparse.ArgumentParser(description='Divvy fencers between pools')
#parser.add_argument('-f', '--file', metavar='', type=argparse.FileType('r'), required=True, help='file with fencer data')
parser.add_argument('-f', '--file', metavar='', required=True, help='file with fencer data')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print only minimumly-needed content to screen')

args = parser.parse_args()

"""Main module."""
if __name__ == '__main__':
    """Entry point."""
    print "Pool creator is now running... \n"

    if not args.file:
        print 'A data file is needed'

    file = args.file.strip()
    isQuiet = args.quiet
    display = Display(isQuiet)
    dataReader = DataReader(file, isQuiet)

    display.print_info('File: %s. isQuiet: %s' % (args.file, args.quiet))
    display.print_info('Reading in csv')
    rawCsv = dataReader.csv()

    if not rawCsv:
        display.print_error('Exiting...')
        exit(-1)
    else:
        display.print_info('csv file read')

    fencersModel = []

    for player in rawCsv:
        if not player:
            print_warning('Fencer value read from csv data file is empty. Entry will be skipped')
            continue

        if not player[3]:
            print_warning('Skill level required to place a fencer. Entry will be skipped')
            continue

        if not player[0]:
            print_warning('At least a last name is needed to identify a fencer. Entry will be skipped')
            continue

        fencer = Fencer(player)
        fencersModel.append(fencer)

    poolService = PoolService(fencersModel)
    pools = poolService.getPools()

    display.print_pools_to_screen(pools)
