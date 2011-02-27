#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Calculate the area of the polygon.
# Copyright (c) 2011, Nycholas de Oliveira e Oliveira <nycholas@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# * Neither the name of the Nycholas de Oliveira e Oliveira nor the names of
#    its contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
import sys
if sys.hexversion < 0x02060000:
    print 'This script requires Python 2.6 or later.'
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
    logging.debug('In polygon_area.main()')
    parser = optparse.OptionParser(
        usage='Usage: %prog [options]',
        version='%prog ' + str(__version__))
    parser.add_option('-c', '--command',
                      action='store_true', dest='is_command', default=False,
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
        from polygon_area.figures.polygon import Polygon
        
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
        print 'Polygon area: %.2f u.a.' % area
        sys.exit(0)

    # Convert string in dictionary!
    opts = eval(str(options))

    from polygon_area.gui.main import Application
    app = Application(args)
    app.mainLoop()
    
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
