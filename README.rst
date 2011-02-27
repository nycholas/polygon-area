area-polygon
============

Calculate the area of the polygon.


Method
******

You need to know the coordinates of the vertices (corners) of the
polygon.  For a state, you could determine those with a GPS device or
through surveying.  Each vertex will have coordinates with respect to
some coordinate system, like (x1,y1), (x2,y2),...,(xn,yn), where 'n'
is the last vertex.  With that information, there is a formula for
calculating the area.  I can give you a reference to a web site that
explains the formula:

`Polygon Area`:

If, for example, you have a plot of land with five vertices (x1,y1),
(x2,y2),(x3,y3),(x4,y4) and (x5,y5), the area would be

    A = (1/2)(x1*y2 - x2*y1 + x2*y3 - x3*y2 + x3y4 - x4y3 + x4*y5 - x5*y4 + x5*y1 - x1*y5)


Referencies
***********

* http://mathworld.wolfram.com/PolygonArea.html
* http://mathforum.org/library/drmath/view/64552.html
* http://matemagicasenumeros.blogspot.com/2011/02/mate-magica-na-area.html


Installation
************

$ python setup.py install


Usage
*****

    $ area_polygon.py --command
    Number of vertices: 3
    Vertice (X, Y): 30,28
    Vertice (X, Y): 30,33
    Vertice (X, Y): 50,30
    --------------------
    The area of the polygon: 50.00


Dependecies
***********

* Python 2.4 or later (http://www.python.org)


Project Information
*******************

`Author:` Nycholas de Oliveira e Olivera
`License:` New BSD License
