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

from ...figures.polygon import Polygon
from vertice import Vertice
from segment import Segment


class GraphScene(QtGui.QGraphicsScene):
    
    def __init__(self, parent=None):
        super(GraphScene, self).__init__(parent)
        self._vertices = []
        self.isPaint = True
        self.polygon = Polygon()
        self.polygonArea = 0.0
        self.updateWidgets()
        
    def mousePressEvent(self, event):
        super(GraphScene, self).mousePressEvent(event)
        pt = event.scenePos()
        print 'click: %s' % pt
        
        if QtCore.Qt.LeftButton == event.button() and self.isPaint:
            self.addVertice(self.createVertice(pt))
        elif QtCore.Qt.RightButton == event.button():
            if self.isPaint:
                vertice = self.createVertice(pt)
                for item in self.items():
                    if item.collidesWithItem(vertice):
                        self.addVertice(item, lastVertice=True)
                        self.createPolygon()
                        self.isPaint = False
                        break
                        
    def updateWidgets(self):
        self.setSceneRect(0.0, 0.0, 100.0, 100.0)
                        
    def createText(self, st, x, y):
        qst = QtCore.QString(st)
        
        font = QtGui.QFont()
        font.setPointSize(font.pointSize() * 1)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font.setBold(True)
        
        fontMetrics = QtGui.QFontMetrics(font)
        textHeight = fontMetrics.height()
        textWidth = fontMetrics.width(qst)
        
        text = QtGui.QGraphicsTextItem(qst)
        text.setDefaultTextColor(QtCore.Qt.black)
        text.setPos(x + 3, y + 3)
        text.setFont(font)
        return text
        
    def createTextVertice(self, vertice):
        (x, y) = (vertice.pos().x(), vertice.pos().y())
        st = '(%.2f, %.2f)' % (x, y)
        qst = QtCore.QString(st)
        
        font = QtGui.QFont()
        font.setPointSize(font.pointSize() * 0.8)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font.setBold(False)
        
        fontMetrics = QtGui.QFontMetrics(font)
        textHeight = fontMetrics.height()
        textWidth = fontMetrics.width(qst)
        
        text = QtGui.QGraphicsTextItem(qst)
        text.setDefaultTextColor(QtCore.Qt.black)
        text.setPos(x + 3, y + 3)
        text.setFont(font)
        return text
                        
    def createVertice(self, pt):
        vertice = Vertice(self)
        vertice.setPos(pt)
        return vertice
    
    def createSegment(self, vt1, vt2):
        segment = Segment(self)
        segment.setPos(vt1, vt2)
        return segment
        
    def createPolygon(self):
        # Adds vertices to the polygon except the last, because 
        # this is already accounted for (repeated)
        for vertice in self._vertices[:-1]:
            self.polygon.add_vertice([vertice.pos().x(),
                                      vertice.pos().y()])
        self.polygonArea = self.polygon.calc_area()
        
        # TODO: Take away, ;-)
        st = 'Polygon area: %.2f u.a.' % self.polygonArea
        (x, y) = (-self.width() / 2.0, self.height() / 2.0)
        self.addItem(self.createText(st, x, y))
                    
    def addVertice(self, vertice, lastVertice=False):
        # Draw vertice, if it does not exist in the list of vertices or 
        # if it is the last vertex of the polygon
        if vertice not in self._vertices or lastVertice:
            # Draw vertice
            self.addItem(vertice)
            
            # Draw text of the coordinates of vertice
            if not lastVertice:
                self.addItem(self.createTextVertice(vertice))
                
            # Add vertice in list
            self._vertices.append(vertice)
            
        # Draw segment
        vertices = self._vertices
        if len(vertices) == 2:
            self.addItem(self.createSegment(vertices[0], vertices[1]))
        elif len(vertices) > 2:
            self.addItem(self.createSegment(vertices[-1], vertices[-2]))
            
    def removeVertice(self, vertice):
        try:
            self.removeItem(vertice)
            self._vertice.remove(vertice)
        except KeyError:
            pass
