Viewing vs editing 
==================

In most cases, information should be presented by default for viewing,
not editing. Presenting input controls to the user when they are not needed
creates unnecessary clutter and distraction, interfering with effective
presentation of the information.

When to use
-----------

Only show editing controls when appropriate. Examples include:

-  When an item is selected, contextually-appropriate editing controls can be
   shown in a toolbar or panel.
-  If an explicit editing mode is appropriate, then editing controls should
   not be shown until that mode is activated.

How to use
----------

.. image:: /img/ViewMode.png
   :alt: Viewing

-  Do not use input controls to show information unless there is an
   explicit request to edit the information.
-  Follow the typography, alignment, and spacing guidelines to layout
   information in a way that is easy to understand.
-  Provide a clear visual hierarchy (where to look first, where to look
   next). The example above uses a large contact photo to anchor the
   layout and the contact name is set in large type to direct the users
   eye to next piece of information.
-  Provide a separate mode for editing the data when requested by the
   user (via a button, toolbutton or menu item):

.. image:: /img/EditMode.png
   :alt: Editing

Inline editing
~~~~~~~~~~~~~~

Inline editing is a feature of some controls. For example, 
:doc:`table views </components/editing/tableview>` are controls that can be used 
for editing purpose as well. When the user accesses an editable cell, usually 
by clicking the cell, its behavior (and appearance) is changed from viewing mode 
to an editing control. The input control can be applied as an unconstrained edit 
or as constrained input, e.g. selection from a predefined set using a 
:doc:`drop-down  </components/editing/dropdown>`. The advance of direct 
input is a concise layout since no additional control is needed for input. The 
drawback is reduced discoverability for table view with restricted editing 
function, at least when only a few cells can be changed. The user does not know 
which cell is editable and which is not. Furthermore, native access via tab or 
access key is not available within a table which means keyboard navigation 
needs to be implemented. 

.. image:: /img/PartialEditMode.png
   :alt: Line-in editing
