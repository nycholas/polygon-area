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
        
    def boundingRect(self):
        adjust = 2
        return QtCore.QRectF(-10 - adjust, -10 - adjust,
                             23 + adjust, 23 + adjust)
        
    def shape(self):
        path = QtGui.QPainterPath()
        path.addEllipse(-5, -5, 5, 5)
        return path
        
    def paint(self, painter, option, widget):
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtCore.Qt.darkGray)
        painter.drawEllipse(-2.5, -2.5, 3.5, 3.5)
        
        gradient = QtGui.QRadialGradient(-2.5, -2.5, 5)
        if option.state & QtGui.QStyle.State_Sunken:
            gradient.setCenter(2.5, 2.5)
            gradient.setFocalPoint(2.5, 2.5)
            gradient.setColorAt(1, QtGui.QColor(QtCore.Qt.yellow).light(120))
            gradient.setColorAt(0, QtGui.QColor(QtCore.Qt.darkYellow).light(120))
        else:
            gradient.setColorAt(0, QtCore.Qt.yellow)
            gradient.setColorAt(1, QtCore.Qt.darkYellow)
        painter.setBrush(gradient)
        painter.setPen(QtGui.QPen(QtCore.Qt.black, 0))
        painter.drawEllipse(-5, -5, 5, 5)
            
            
