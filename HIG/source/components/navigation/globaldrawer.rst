Global Drawer
=============

Purpose
-------

The Global Drawer is a standard element in KDE mobile applications. It
contains an application's main menu, and any functions which are not
part of the application's main usecases but are not specific to the
current context either.

.. container:: intend

   |desktopicon| |mobileicon|

.. container:: available plasma qwidgets

   |nbsp|


.. figure:: /img/Globaldrawer1.png
   :alt: Global drawer on mobile
   :figclass: border
   :scale: 40 %

   Global drawer on mobile

Guidelines
----------

Is this the right control?
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /img/Globaldrawer3.png
   :figclass: border
   :alt: Global drawer on desktop
   :scale: 40 %

   Global drawer on desktop
   
Use a Global Drawer whenever your application has any functions which
are not central enough to the application's main purpose to put them in
the main user interface, and which are not dependent on the current
context. For context-specific actions (e.g. those affecting a selected
item), use the :doc:`Context Drawer <contextdrawer>`

Behavior
~~~~~~~~

.. figure:: /img/Globaldrawer2.png
   :alt: Global drawer on desktop
   :scale: 40 %
   :figclass: border

   Hamburger button on the toolbar on desktop.

The Global Drawer is either opened by clicking on the hamburger button on the 
toolbar or by swiping from the left edge of the screen. It can be closed by 
swiping in the other direction, clicking the close button or tapping outside of 
it.

A Global Drawer may contain the following controls:

-  :doc:`Tabs <tab>`
-  A main menu
-  :doc:`Push Buttons <pushbutton>` to execute non-contextual actions
-  :doc:`Checkboxes <../editing/checkbox>` 
   or :doc:`Radio Buttons <../editing/radiobutton>` 
   to change settings which are commonly changed

The main menu

-  Must not have more than three levels
-  Should if possible not contain more elements than fit on the screen
-  Should contain an entry :doc:`Settings </platform/settings>` in the last
   position if the application has settings which are not commonly changed
-  Selecting an entry in the menu either executes an action or goes down
   one level, replacing the menu with the items in the selected submenu
-  In lower menu levels, below the entries there is a button to go up
   one level.

Don't use the Menu Drawer for navigation purposes.

|desktopicon| Collapsible
"""""""""""""""""""""""""

On the desktop, if the elements in the Global Drawer need to be accessed more 
often and enough space is available, the Global Drawer can default to showing a 
collapsed state, where the labels disappear but all actions continue to be 
available via icons-only ToolButtons. Pressing the hamburger menu button 
expands the Global Drawer to its full width and shows the actions' text 
labels. Pressing the close button or anywhere outside of it collapses it to its 
collapsed icons-only state.

.. raw:: html

   <video src="https://cdn.kde.org/hig/video/20201214/Globaldrawer4.webm" 
   loop="true" playsinline="true" width="640" controls="true" 
   onended="this.play()" class="border"></video>

Code
----

Kirigami
~~~~~~~~

 - :kirigamiapi:`Kirigami: GlobalDrawer <GlobalDrawer>`

 .. literalinclude:: /../../examples/kirigami/AddressbookGlobalDrawer.qml
   :language: qml
