Settings
========

A settings provide the ability to customize how an application, a Plasma widget 
or the Plasma Workspace looks or should behave. It is intended for settings that 
are persistent but not changed very frequently. 


Settings for the Plasma Workspace are often referred to as KCM KConfig Modules. 
They can either appear in Plasmas System Setting or as standalone configuration 
dialog.

Example
-------

.. figure:: /img/Settings-dark.png
   :alt: Buttons on the bottom of the settings
   :scale: 60%

Guidelines
----------

When to Use
~~~~~~~~~~~

-  Use the settings page to display settings that are persistent but not
   accessed or changed very frequently. The toolbar or the main menu (and optionally context menus) are more appropriate places for settings that
   are frequently accessed and changed, such as icon view style or sort order.
-  Don't use settings pages to change the properties of a selected item.
   Instead, use a properties dialog or a contextual editing panel.
-  Don't use the settings page for potentially dangerous developer settings
   like the name of an SQL table. Instead, use configuration files or separate
   dialogs.

How to Use
~~~~~~~~~~

-  **Simple by default**: Define smart and polite defaults so that your target
   :doc:`personas </introduction/personas>` don't have to alter them at all.
-  **Powerful when needed**: Provide enough settings for the perfect
   customization according individual needs and preferences. But even
   though customizability is very important for KDE software, try to
   keep your settings page as small and simple as possible. Remember:
   every option requires more code and more testing, and makes the settings
   page slower to use.
-  Respect the privacy of the users: Always use opt-in, never an opt-out
   model for features that transmit potentially private data (e.g. usage
   statistics). See KDE's 
   `Telemetry Policy <https://community.kde.org/Policies/Telemetry_Policy>`_
   for details.
-  Following KDE's "Simple by default, powerful when needed" 
   :doc:`design mantra </index>`, settings can be split into common and 
   advanced groups. Advanced settings are not important to most users but 
   essential for some, and therefore cannot be removed. Those settings are 
   hidden by default to reduce the mental overhead of using the settings page, 
   but with easy access.


Behavior
~~~~~~~~

-  When a change is applied, the application should adopt it immediately
   without the need to restart it.
-  Don't change the settings page depending on the context. It
   should always start with the same landing page regardless of the
   application context.
-  Don't use a wizard to change settings. Only use a wizard if a group of
   settings are all interrelated and must be edited all at once, e.g.
   setting up an email account.
-  If some of the program's settings are only applicable in certain contexts,
   don't hide the inapplicable ones. Instead, disable them and hint to the
   user why they're disabled.
   **Exception:** it is acceptable to hide settings for non-existent hardware.
   For example, it's okay to hide the touchpad configuration when no touchpad
   is present.
-  Consider adding access to third-party add-ons via 
   :doc:`Get New Stuff! <getnew>`.
-  Ctrl + Tab should switch between logical groups of controls.

.. attention::
   |devicon| For :doc:`accessiblity </accessibility/index>` make sure to test 
   keyboard navigation with the settings. Make sure to set the focus to focused 
   controls and don't just highlight it.
   
Appearance
~~~~~~~~~~

-  For a desktop app, put your settings page inside a dialog window.
-  Place buttons at the bottom of the settings. The *Apply* to the right, an 
   optional :doc:`Get New Stuff! <getnew>` button to the right above the Apply 
   button.
   
   .. figure:: /img/SettingsButtons.png
      :alt: Buttons on the bottom of the settings
      :scale: 60%
      :figclass: border
      
   The *Help*, *Defaults*, *Reset* buttons on the left side.

-  You should avoid vertical and especially horizontal scrollbars. 
   Separate your controls into more groups and make use of 
   :doc:`tabbed views </components/navigation/tab>`. 
   This does not apply to scrollbars within inline tables, lists and grid 
   views.
-  On mobile, use a full-screen view for your settings page.

**There are several well established layouts for settings that are used threw 
KDE software.**

Forms
"""""

.. figure:: /img/Settings-Notification-dark.png
   :alt: Notifications settings in a form layout
   :scale: 40%
   
   Notifications settings in a form layout
   
Use a :doc:`form </patterns/content/form>` if your setting consist of may 
controls and input fields.

-  Lay out your settings page according to the
   :doc:`alignment </layout/alignment>` guidelines.
-  Organize your settings into logical groups, with more important groups
   appearing higher up on the page. Separate the groups with white space or
   put them into different tabs of a
   :doc:`tabbed view </components/navigation/tab>` (if appropriate).
-  Separate common and advanced settings into different groups. If necessary,
   hide the advanced settings behind a collapsible group box. Make the
   standard settings comprehensible and easy to use.

Grid
""""

.. figure:: /img/Wallpaper-dark.png
   :alt: Choose a new Plasma Design
   :scale: 40%
   
   Choose a new wallpaper

Use a :doc:`grid </components/editing/grid>` for a visual selection of a 
single option. To implement grids in KCM Modules use the 
:doc:`KCMGrid <kcmgrid>`.

Lists
"""""

.. figure:: /img/LanguagePicker.png
   :alt: Language settings
   :scale: 60%
   
   Language settings

Use a :doc:`picker </patterns/content/picker>` for selection and configuration 
of list based settings


.. Mockup
.. ~~~~~~
.. 
.. .. image:: /img/HIG-Settings.png
..    :alt: HIG-Settings.png
.. 
.. 
.. #. Access groups via sidebar.
.. #. The preview has to be on the top of the content area.
.. #. Offer a good number of pre-defined profiles/schmes to let the user
..    choose one out of different factory settings. Anchor the profiles so
..    that users can have more space for the area below using the
..    horizontal splitter. Cut long captions with ellipsis and show the
..    full name in a tooltip.
..    (Remark 1: The mockup has very large splitters. The implementation
..    should be visually less obtrusive.)
..    (Remark 2: The profile selection replaces the former "reset (to
..    default)" function.)
.. #. Allow users to add more profiles via Get Hot New Stuff (GHNS).
..    Organize the setting in a way that GHNS access is per group and not
..    global.
.. #. Provide access to the most relevant settings at the Standard section.
..    Make sure that these settings are easy to understand.
.. #. Indicate that Advanced settings are available but keep this section
..    collapsed by default. Use a descriptive label so that it reflects the
..    functionality.
.. #. Allow users to export the current settings to a file that can be
..    easily imported on any other machine.
.. #. Allow to Apply the current settings to the application without
..    closing the dialog.
.. #. Provide access to functions for user-defined profiles per context
..    menu and standard shortcuts.
.. #. Scroll the whole area of options but neither the preview not the
..    profiles, if necessary.
