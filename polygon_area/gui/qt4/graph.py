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
from PySide import QtCore, QtGui

from scene import GraphScene


class GraphWidget(QtGui.QGraphicsView):
    
    def __init__(self, parent=None):
        super(GraphWidget, self).__init__(parent)
        self.createWidgets()
        self.updateWidgets()
        self._points = []
        self._vertices = []
    
    def createWidgets(self):
        self.setObjectName("GraphWidget")
        self.scene = GraphScene(self)
        self.scene.setItemIndexMethod(QtGui.QGraphicsScene.NoIndex)
        self.scene.setSceneRect(-200, -200, 400, 400)
        
    def updateWidgets(self):
        self.setScene(self.scene)
        #self.setCacheMode(CacheBackground)
        #self.setViewportUpdateMode(BoundingRectViewportUpdate)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        #self.setTransformationAnchor(AnchorUnderMouse)
        self.scale(0.8, 0.8)
        self.setMinimumSize(400, 400)
        self.setWindowTitle("Polygon Area")
    
    def addPoint(self, pt):
        if not pt in self._points:
            self._points.append(pt)
        
        vertice = Vertice(self)
        self.scene.addItem(vertice)
            
        if len(self._points) == 2:
            line = QtGui.QGraphicsLineItem(
                QtCore.QLineF(self._points[0],
                             self._points[1]))
            self.scene.addItem(line)
            #self.addLine(self._points[0].x(), self._points[0].y(),
            #             self._points[1].x(), self._points[1].y())
        elif len(self._points) > 2:
            #self.addLine(self._points[-2].x(), self._points[-2].y(),
            #             self._points[-1].x(), self._points[-1].y())
            line = QtGui.QGraphicsLineItem(
                QtCore.QLineF(self._points[-2],
                             self._points[-1]))
            self.scene.addItem(line)
    def removePoint(self, pt):
        try:
            self._points.remove(pt)
        except KeyError:
            pass
