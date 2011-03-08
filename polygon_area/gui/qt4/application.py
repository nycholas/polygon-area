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

from PySide import QtCore, QtGui


class Application(QtGui.QApplication):
    
    def __init__(self, argv, *args, **kwargs):
        super(Application, self).__init__(argv)
        
        # Command line arguments
        (args, options) = args
        
        self.__mainWindow = None

        self.isTest = options.get('is_test', False)
        self.isLogging = options.get('is_logging', False)
        self.isDebug = options.get('is_debug', False)
        
    @property
    def mainWindow(self):
        return self.__mainWindow
        
    def mainLoop(self):
        from mainwindow import MainWindow
        
        # Initialize main window
        self.__mainWindow = MainWindow()
        
        # Check is a test
        if self.isTest:
            self.__mainWindow.createTest()
        
        # Show main window
        self.__mainWindow.show()
        
        # Actions
        if not QtGui.QSystemTrayIcon.isSystemTrayAvailable():
            self.connect(self, QtCore.SIGNAL("lastWindowClosed()"), 
                         self, QtCore.SLOT("quit()"))
        
        # Exec main loop
        sys.exit(self.exec_())
        

if __name__ == '__main__':
    app = Application()
    app.mainLoop()
