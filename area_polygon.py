#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
if sys.hexversion < 0x02040000:
    print 'This script requires Python 2.4 or later.'
    print 'Currently run with version: %s' % sys.version
    print 'Please install it. The source for Python can be found at: ' \
          'http://www.python.org/.'
    sys.exit(-1)
import os
import logging
import optparse

# Include base path in sytem path for Python old.
syspath = os.path.abspath(os.path.dirname(__file__))
if not syspath in sys.path:
    sys.path.append(syspath)

__version__ = 0.1

def main(args):
    logging.debug('In area_polygon.main()')
    parser = optparse.OptionParser(
        usage='Usage: %prog [options]',
        version='%prog ' + str(__version__))
    parser.add_option('-c', '--command',
                      action='store_true', dest='is_command', default=True,
                      help='Terminal mode')
    parser.add_option('-t', '--test',
                      action='store_true', dest='is_test', default=False,
                      help='Test application with forward')
    parser.add_option('-l', '--logging',
                      action='store_true', dest='is_logging', default=False,
                      help='Logging console mode')
    parser.add_option('-v', '--verbose',
                      action='store_true', dest='is_debug', default=False,
                      help='Verbose (debug) mode')
    (options, args) = parser.parse_args()
    logging.debug(':: options: %s' % options)
    logging.debug(':: args: %s' % args)

    if options.is_command:
        from area_polygon.figures.polygon import Polygon
        
        number_vertices = input('Number of vertices: ')

        # Checks that the number of vertices
        if not isinstance(number_vertices, int):
            if not str(number_vertices).isdigit():
                parser.error('Invalid number of vertices')
            number_vertices = int(number_vertices)

        # Checks that the number of vertices is greater than or
        # equal to 3
        if number_vertices < 3:
            parser.error('The number of vertices must be greater than or ' \
                         'equal to 3')
        
        polygon = Polygon()
        for i in xrange(number_vertices):
            vertice = input('Vertice (X, Y): ')

            if not isinstance(vertice, tuple):
                # Checks whether the format of the vertice
                if str(vertice).find(',') == -1:
                    parser.error('Vertice must be of the form: X, Y')

                # Checks that the number of vertices is integers
                try:
                    vertice = [int(i.strip()) for i in vertice.split(',')]
                except ValueError, e:
                    parser.error('Vertice must be of the form (integers): X, Y')
            else:
                # Checks that the number of vertices is integers
                try:
                    vertice = [int(i) for i in vertice]
                except ValueError, e:
                    parser.error('Vertice must be of the form (integers): X, Y')

            # Add vertice in polygon
            polygon.add_vertice(vertice)
        area = polygon.calc_area()
        
        print '-' * 20
        print 'The area of the polygon: %.2f' % area
        sys.exit(0)

    # Convert string in dictionary!
    opts = eval(str(options))

    
if __name__ == '__main__':
    import sys
    main(sys.argv)