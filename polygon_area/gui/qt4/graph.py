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
from PySide import QtCore, QtGui

from scene import GraphScene


class GraphWidget(QtGui.QGraphicsView):
    
    def __init__(self, index, parent=None):
        super(GraphWidget, self).__init__(parent)
        self.index = index
        self.createWidgets()
        self.updateWidgets()
        
    def mouseMoveEvent(self, event):
        super(GraphWidget, self).mouseMoveEvent(event)
        pt = event.pos()
        self.statusBarShowMessage('Coordinate (%2.f, %2.f)' % (pt.x(), pt.y()))
    
    def createWidgets(self):
        self.scene = GraphScene(self)
        self.scene.setItemIndexMethod(QtGui.QGraphicsScene.NoIndex)
        self.scene.setSceneRect(-200, -200, 400, 400)
        
    def updateWidgets(self):
        self.setObjectName('GraphWidget-%d' % self.index)
        self.setScene(self.scene)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.scale(0.8, 0.8)
        self.setMinimumSize(400, 400)
        self.setWindowTitle(
            QtGui.QApplication.translate('GraphWidget-%d' % self.index, 
                                         'Polygon Area', 
                                         None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.setMouseTracking(True)
        
    def statusBarShowMessage(self, st):
        qst = QtCore.QString(st)
        mainWindow = QtGui.qApp.mainWindow
        mainWindow.statusBar().showMessage(qst)

