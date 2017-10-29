"""Entry point to the application."""
import argparse
import os
import platform

from service.display import Display
from service.csvReader import CsvReader
from service.pool import Pool as Pool_Service
from model.pool import Pool as Pool_Model
from model.fencer import Fencer

parser = argparse.ArgumentParser(description='Divvy fencers between pools')
parser.add_argument('file', type=str, help='File with data')
group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbose', action='store_true', help='print debugging information ')

args = parser.parse_args()

"""Main module."""
if __name__ == '__main__':
    """Entry point."""
    if platform.system() == 'Linux':
        clear = 'clear'
    else:
        clear = 'cls'

    os.system(clear)

    print "Pool creator is now running... \n"

    if not args.file:
        print 'A data file is needed'

    file = args.file.strip()
    is_verbose = args.verbose
    display = Display(is_verbose)
    csvReader = CsvReader(file, is_verbose)

    display.print_info('File: %s. is_verbose: %s' % (args.file, args.verbose))
    display.print_info('Reading in csv')
    raw_csv = csvReader.read()

    if not raw_csv:
        display.print_error('Exiting...')
        exit(-1)
    else:
        display.print_info('csv file read')

    fencers_model = []

    for f in raw_csv:
        if not f:
            display.print_error('Invalid read. Fencer info is not set in file-line.')
            continue

        if not f[3]:
            display.print_error('Invalid fener. Skill level required.')
            continue

        if not str.isalpha(f[3][0]):
            display.print_error('Invalid skill in fencer. First character is not an alphabet')
            continue

        year = f[3][1:]
        if year:
            try:
                int(year)
            except ValueError:
                display.print_error('Invalid skill. The year is not a number')
                continue

        if not f[0]:
            display.print_warning('Invalid fencer. Fencer needs a last name.')
            continue

        fencer = Fencer(f)
        fencers_model.append(fencer)

    fencers_model = sorted(fencers_model, key=lambda f:f.numeric_skill_level, reverse=True)
    pool_service = Pool_Service(fencers_model)
    pools = pool_service.get_pools()

    display.print_fencers_to_screen(fencers_model)
    display.print_pools_to_screen(pools)
