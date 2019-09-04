Grid
====

Grids are, similar to tables, a structure to distribute items into rows and 
columns. Contrary to tables grids dont have a fixed structure, but columns and 
rows are detemend b the available space.



.. image:: /img/GridWallpapers.png
   :alt:  Grid

Guidelines
----------

Behavior
~~~~~~~~

Grids adjust the number of rows and columns dynamically to distribute the items 
to the available space. If the not enough space is available vertical scolling 
is enabled.

You can apply :doc:`on demand controls </patterns/command/ondemand>` to the 
items.


Appearance
~~~~~~~~~~

-  All items must be the same size.
-  All rows, except the last one, have the same number of items
-  Overlay buttons are placed at the bottom right corner of items.
-  Grids have a PaperWhite background on desktop, and no background on
   mobile.

Code
----

Kirigami
~~~~~~~~

 - `QML: GridView <https://doc.qt.io/qt-5/qml-qtquick-gridview.html>`_
 - :kirigamiapi:`Kirigami: CardsGridView <CardsGridView>`

Use of KCMGrid in Plasmas System Settings

.. literalinclude:: /../../examples/kirigami/KCMGrid.qml
   :language: qml
