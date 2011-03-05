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


class Vertice(QtGui.QGraphicsItem):
    
    def __init__(self, graphicScene, parent=None):
        super(Vertice, self).__init__(parent)
        self._diameter = 30
        self._radius = self._diameter / 2.0
        self._penWidth = 0
        self._bounds = [-self._diameter * 0.5, -self._diameter * 0.5, 
                        self._diameter, self._diameter]
        self._adjust = self._diameter * 0.1
        self.updateWidgets()
        
    def boundingRect(self):
        rect = QtCore.QRectF(self._bounds[0] - self._adjust, 
                             self._bounds[1] - self._adjust,
                             self._bounds[2] + self._adjust, 
                             self._bounds[3] + self._adjust)
        return rect
        
    def shape(self):
        path = QtGui.QPainterPath()
        path.addEllipse(self._bounds[0], self._bounds[1],
                        self._bounds[2], self._bounds[3])
        return path
        
    def paint(self, painter, option, widget):
    
        # Draw the shadow ellipse
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtCore.Qt.darkGray)
        painter.drawEllipse(self._bounds[0]*0.5, self._bounds[1]*0.5,
                            self._bounds[2]*0.8, self._bounds[3]*0.8)
        
        gradient = QtGui.QRadialGradient(-self._radius * 0.3, 
                                         -self._radius * 0.3, 
                                         self._radius * 0.8)
        if option.state & QtGui.QStyle.State_Sunken:
            gradient.setCenter(self._radius, self._radius)
            gradient.setFocalPoint(self._radius, self._radius)
            gradient.setColorAt(0, 
                                QtGui.QColor(QtCore.Qt.darkYellow).darker(120))
            gradient.setColorAt(1, QtGui.QColor(QtCore.Qt.yellow).darker(120))
        else:
            gradient.setColorAt(0, QtCore.Qt.yellow)
            gradient.setColorAt(1, QtCore.Qt.darkYellow)
        
        # Draw the ellipse itself
        painter.setBrush(gradient)
        painter.setPen(QtGui.QPen(QtCore.Qt.black, self._penWidth))
        painter.drawEllipse(self._bounds[0], self._bounds[1],
                            self._bounds[2], self._bounds[3])
                            
    def mousePressEvent(self, event):
        super(Vertice, self).mousePressEvent(event)
        self.update()
        
    def mouseReleaseEvent(self, event):
        super(Vertice, self).mouseReleaseEvent(event)
        self.update()
    
    def mouseMoveEvent(self, event):
        super(Vertice, self).mouseMoveEvent(event)
        self.update()
            
    def updateWidgets(self):
        #self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtGui.QGraphicsItem.ItemSendsGeometryChanges)
        self.setCacheMode(QtGui.QGraphicsItem.CacheMode.DeviceCoordinateCache)
        self.setZValue(1)
