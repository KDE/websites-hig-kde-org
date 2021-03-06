Status Icons
============

Status icons are used to indicate the status of hardware and software.
They come in two sizes: 16px, 22px, and use the `monochrome style <index.html>`__.

Purpose
-------

Status icons allow a user to discern the current state of hardware and software
at a glance. They reassure users that software is functional, and warn them when
hardware is dysfunctional.

Design
------

Anatomy
~~~~~~~

Base
++++

The base of a status icon indicates to the user what item the state of the icon
represents.

.. container:: flex

   .. container::

      .. figure:: /img/status-base-do.png
         :scale: 80%
         :figclass: do

         :noblefir:`Do.` |br|
         Use a simple and recognizable icon base that leaves
         room for additions to indicate state.

   .. container::

      .. figure:: /img/status-base-dont.png
         :scale: 80%
         :figclass: dont

         :iconred:`Don't.` |br|
         Don't use an overly simple base—this makes it hard for
         the user to identify what an icon represents. Additionally,
         don't use more details than you need to make something recognizable—
         this doesn't leave you room for indicating states.

Overlay
+++++++

The overlay of a status icon indicates to the user what status the item the icon
represents is in.

.. container:: flex

   .. container::

      .. figure:: /img/status-overlay-do.png
         :scale: 80%
         :figclass: do

         :noblefir:`Do.` |br|
         Use a simple and recognizable overlay with appropriately used color
         to clue in the user to an icon's status.

   .. container::

      .. figure:: /img/status-caution.png
         :scale: 80%
         :figclass: caution

         :ambientamber:`Caution.` |br|
         Some overlays can be hard to identify on their own—provide appropriate
         context to allow a user to identify what a simple icon represents.

.. container:: flex

   .. container::

      .. figure:: /img/status-overlay-dont-color.png
         :scale: 80%
         :figclass: dont

         :iconred:`Don't.` |br|
         Don't exclusively rely on colour to indicate state—this is an accessibility
         problem and makes it hard to discern state.

   .. container::

      .. figure:: /img/status-overlay-dont-detail.png
         :scale: 80%
         :figclass: dont

         :iconred:`Don't.` |br|
         Don't use too-generic details to represent state—this makes it hard for
         a user to identify what an icon's state represents.