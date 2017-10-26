"""Entry point to the application."""
import argparse

from service.display import Display
from service.dataReader import Data_Reader
from service.pool import Pool as Pool_Service
from model.pool import Pool as Pool_Model
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
    is_quiet = args.quiet
    display = Display(is_quiet)
    data_reader = Data_Reader(file, is_quiet)

    display.print_info('File: %s. is_quiet: %s' % (args.file, args.quiet))
    display.print_info('Reading in csv')
    raw_csv = data_reader.csv()

    if not raw_csv:
        display.print_error('Exiting...')
        exit(-1)
    else:
        display.print_info('csv file read')

    fencers_model = []

    for player in raw_csv:
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
        fencers_model.append(fencer)

    pool_service = Pool_Service(fencers_model)
    pools = pool_service.get_pools()

    display.print_pools_to_screen(pools)
