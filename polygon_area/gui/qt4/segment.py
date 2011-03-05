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
import math

from PySide import QtCore, QtGui


class Segment(QtGui.QGraphicsItem):
    PI = math.pi
    TWO_PI = math.pi * 2.0
    
    def __init__(self, graphicScene, parent=None):
        super(Segment, self).__init__(parent)
        self._penWidth = 1
        self._arrowSize = 100
        self._vt1 = QtCore.QPointF(0, 0)
        self._vt2 = QtCore.QPointF(0, 0)
        self.updateWidgets()
        
    def setPos(self, vt1, vt2):
        self._vt1 = vt1
        self._vt2 = vt2
    
    def pos(self):
        return (self._vt1, self._vt2)
        
    def boundingRect(self):
        extra = (self._penWidth + self._arrowSize) / 2.0
        rect = QtCore.QRectF(self.mapFromItem(self._vt1, 0, 0), 
                             self.mapFromItem(self._vt2, 0, 0)) \
            .normalized() \
            .adjusted(-extra, -extra, extra, extra)
        return rect
            
    def shape(self):
        path = QtGui.QPainterPath()
        #path.addRect(self.mapFromItem(self._vt1, 0, 0),
        #             self.mapFromItem(self._vt2, 0, 0),
        #             1, 1)
        return path
        
    def paint(self, painter, option, widget):
        line = QtCore.QLineF(self.mapFromItem(self._vt1, 0, 0), 
                             self.mapFromItem(self._vt2, 0, 0))
        
        if int(line.length()) == 0:
            return
            
        # Draw the line itself
        painter.setPen(QtGui.QPen(QtCore.Qt.black, self._penWidth, 
                                  QtCore.Qt.SolidLine, QtCore.Qt.RoundCap,
                                  QtCore.Qt.RoundJoin))
        painter.setBrush(QtCore.Qt.black)
        painter.drawLine(line)
        
    def updateWidgets(self):
        self.setZValue(-1)
            
