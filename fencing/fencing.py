"""Entry point to the application."""
import argparse
import os
import platform

from service.display import Display
from service.csvReader import Csv_Reader
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
    csv_Reader = Csv_Reader(file, is_verbose)

    display.print_info('File: %s. is_verbose: %s' % (args.file, args.verbose))
    display.print_info('Reading in csv')
    raw_csv = csv_Reader.read()

    if not raw_csv or len(raw_csv) == 0:
        display.print_error('Exiting...')
        exit(-1)
    else:
        display.print_info('csv file read')

    fencers_model = []

    for line_num, fencer_entry in raw_csv.items():
        display.print_info('Reading line #{0}'.format(line_num))

        if not fencer_entry:
            display.print_error('Invalid read at line: {0}. Fencer info is not set in file-line.'.format(line_num))
            continue

        if not fencer_entry[3]:
            display.print_error('Invalid fencer at line: {0}. Skill level required.'.format(line_num))
            continue

        if not str.isalpha(fencer_entry[3][0]):
            display.print_error('Invalid skill at line: {0}. First character is not an alphabet'.format(line_num))
            continue

        year = fencer_entry[3][1:]
        if year:
            try:
                int(year)
            except ValueError:
                display.print_error('Invalid skill at line: {0}. The year is not a number'.format(line_num))
                continue

        if not fencer_entry[0]:
            display.print_warning('Invalid fencer at line: {0}. Fencer needs a last name.'.format(line_num))
            continue

        fencer = Fencer(fencer_entry)
        fencers_model.append(fencer)

    fencers_model = sorted(fencers_model, key=lambda f:f.numeric_skill_level, reverse=True)
    pool_service = Pool_Service(fencers_model)
    pools = pool_service.get_pools()

    display.print_fencers_to_screen(fencers_model)
    display.print_pools_to_screen(pools)
