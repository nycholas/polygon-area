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
import os

from PySide import QtCore, QtGui, QtSvg

from widgets.ui_mainwindow import Ui_MainWindow
from graph import GraphWidget


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.graph = None
        self.scene = None
        self.createWidgets()
        self.updateWidgets()
        
    #@property
    #def statusBar(self):
    #    return self.statusBar()
        
    def createTest(self):
        # Crate vertices of polygon
        vertices = [
            self.scene.createVertice(QtCore.QPointF(30, 28)),
            self.scene.createVertice(QtCore.QPointF(30, 33)),
            self.scene.createVertice(QtCore.QPointF(50, 30)),
        ]
        vertices = [
            self.scene.createVertice(QtCore.QPointF(20, 30)),
            self.scene.createVertice(QtCore.QPointF(20, 50)),
            self.scene.createVertice(QtCore.QPointF(40, 35)),
            self.scene.createVertice(QtCore.QPointF(60, 50)),
            self.scene.createVertice(QtCore.QPointF(60, 20)),
            self.scene.createVertice(QtCore.QPointF(50, 5)),
            self.scene.createVertice(QtCore.QPointF(20, 30)),
        ]
        
        # Draw vertices of polygon
        for vertice in vertices:
            self.scene.addVertice(vertice)
        self.scene.addVertice(vertices[0], lastVertice=True)
        
        # Draw polygon
        self.scene.createPolygon()
        
        # Painting hangs
        self.scene.isPaint = False
        
        # Check test
        #assert self.scene.polygonArea == 50.0
        assert self.scene.polygonArea == 1050.0
        
    def createWidgets(self):
        self.graph = GraphWidget(self.centralwidget)
        self.scene = self.graph.scene
        self.gridLayout.addWidget(self.graph, 0, 0, 1, 1)
        
    def updateWidgets(self):
        self.setWindowTitle("Polygon Area")        
        
    def createActions(self):
        pass
        

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
