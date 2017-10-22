"""Entry point to the application."""
import argparse
from service.display import Display

parser = argparse.ArgumentParser(description='Divvy fencers between pools')
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

    dataFile = args.file.strip()
    isQuiet = args.quiet
    display = Display(args.quiet)

    display.print_info('ok')

    print 'file: %s. isQuiet: %s' % (args.file, args.quiet)
