Grid
====

Grids are, similar to tables, a structure to distribute items into rows and 
columns. Contrary to tables grids dont have a fixed structure, but columns and 
rows are detemend b the available space.



.. image:: /img/GridWallpapers.png
   :alt:  Grid

Guidelines
----------

Is this the right control?
~~~~~~~~~~~~~~~~~~~~~~~~~~

Grids are similar to :doc:`lists <list>` used to display a sortet or unsortet 
number of items. All items should be of the same kind.

Behavior
~~~~~~~~

Grids adjust the number of rows and columns dynamically to distribute the items 
to the available space. If the not enough space is available vertical scolling 
is enabled.

-  Don't have blank grid items; use meta-options, e.g. (None) instead.
-  Place options that represent general options (e.g. All, None) at the
   beginning of the grid.
-  Sort grid items in a logical order. Make sure sorting fits
   translation.

On-Demand Actions
^^^^^^^^^^^^^^^^^

Grid items can uses an :doc:`on-demand pattern </patterns/command/ondemand>` as
an alternative to always-visible controls. If the user often performs tasks on 
single items of a grid, you can add on-demand controls to the grid item for 
these.

Picker
^^^^^^

Grids can be used for the :doc:`picker pattern </patterns/content/picker>`. 
Place a button below the grid to add items to the grid. To remove items from 
the grid, either add an remove action on the item, or give the user the 
possibility to select items and add a global remove button at the bottom of the 
grid.

Ordering
^^^^^^^^

Allow drag and drop of items, if the the order of the items can be 
changed by the user. 

Appearance
~~~~~~~~~~

-  All items must be the same size. Item can change there size, either threw 
   user input or as a response to changes of the available space for the grid.
-  All rows, except the last one, have the same number of items.
-  Use :doc:`sentence style capitalization </style/writing/capitalization>`
   for grid view items.

Cards
^^^^^

See :doc:`cards <card>` for more information how to use cards in a grid view.

KCM
^^^

Use the :doc:`KCMGrid </plattform/kcmgrid>` for grids in KCM modules.

Code
----

Kirigami
~~~~~~~~

 - `QML: GridView <https://doc.qt.io/qt-5/qml-qtquick-gridview.html>`_
