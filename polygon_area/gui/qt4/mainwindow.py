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
import os

from PySide import QtCore, QtGui, QtSvg

from widgets.ui_mainwindow import Ui_MainWindow
from graph import GraphWidget


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self._graphs = []
        self.createWidgets()
        self.updateWidgets()
        
    def mouseMoveEvent(self, event):
        super(MainWindow, self).mouseMoveEvent(event)
        
        qst = QtCore.QString('')
        self.statusBar().showMessage(qst)
        
    #@property
    #def statusBar(self):
    #    return self.statusBar()
        
    def createTest(self):
        # Scene graph
        graph = self._graphs[0]
        scene = graph.scene
    
        # Crate vertices of polygon
        vertices = [
            scene.createVertice(QtCore.QPointF(30, 28)),
            scene.createVertice(QtCore.QPointF(30, 33)),
            scene.createVertice(QtCore.QPointF(50, 30)),
        ]
        vertices = [
            scene.createVertice(QtCore.QPointF(20, 30)),
            scene.createVertice(QtCore.QPointF(20, 50)),
            scene.createVertice(QtCore.QPointF(40, 35)),
            scene.createVertice(QtCore.QPointF(60, 50)),
            scene.createVertice(QtCore.QPointF(60, 20)),
            scene.createVertice(QtCore.QPointF(50, 5)),
            scene.createVertice(QtCore.QPointF(20, 30)),
        ]
        
        # Draw vertices of polygon
        for vertice in vertices:
            scene.addVertice(vertice)
        scene.addVertice(vertices[0], lastVertice=True)
        
        # Draw polygon
        scene.createPolygon()
        
        # Painting hangs
        scene.isPaint = False
        
        # Check test
        #assert self.scene.polygonArea == 50.0
        assert scene.polygonArea == 1050.0
        
    def createWidgets(self):
        self.tabWidget.clear()
        if self.tabWidget.count() == 0:
            self.addGraph(self.createGraph())
        
    def updateWidgets(self):
        self.setWindowTitle(
            QtGui.QApplication.translate('MainWindow', 
                                         'Polygon Area', 
                                         None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.setMouseTracking(True)
        
    def createActions(self):
        pass
        
    def createGraph(self):
        index = self.tabWidget.count()
        graph = GraphWidget(index, self)
        
        #graphGridLayout = QtGui.QGridLayout(self.tabScene0)
        #graphGridLayout.setObjectName('graphGridLayout0')
        #graphGridLayout.addWidget(self.graph, 0, 0, 1, 1)
        
        return graph
        
    def addGraph(self, graph):
        if graph not in self._graphs:
            icon = QtGui.QIcon()
            icon.addPixmap(
                QtGui.QPixmap(
                    ":/media/default/32x32/icons/polygon-area.png"),
                    QtGui.QIcon.Normal, 
                    QtGui.QIcon.Off)
                    
            # Add graph in tabWidget
            qst = QtCore.QString(
                QtGui.QApplication.translate(
                    'MainWindow', 
                    '(Graph %s)' % str(self.tabWidget.count() + 1), 
                    None,
                    QtGui.QApplication.UnicodeUTF8))
            self.tabWidget.addTab(graph, icon, qst)
            self._graphs.append(graph)
        
    def removeGraph(self, graph):
        try:
            self.tabWidget.remove(graph)
            self._graphs.remove(graph)
        except KeyError:
            pass
        

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
