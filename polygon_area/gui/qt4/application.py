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
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
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

try:
    from PySide import QtCore, QtGui, QtOpenGL, QtSvg
except ImportError, e:
    print 'This script requires PySide 4.7 or later'
    print 'Please install it. The source for PySide can be found at: ' \
          'http://www.pyside.org/.'
    print 'Error: %s' % e
    sys.exit(-1)


class Application(QtGui.QApplication):
    
    def __init__(self, args):
        super(Application, self).__init__(args)
        
    def mainLoop(self):
        from mainwindow import MainWindow
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        
        # Exec main loop
        sys.exit(self.exec_())
        

if __name__ == '__main__':
    app = Application()
    app.mainLoop()
