#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# KDE HIG documentation build configuration file, created by
# sphinx-quickstart on Tue Feb  6 13:29:47 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

from sphinx.util.console import bold
import requests
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../..'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.todo', 'sphinxcontrib.doxylink']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Human Interface Guidelines'
copyright = '2019, KDE. Licensed under Creative Commons License SA 4.0'
author = 'KDE'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'KDEHIGdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'KDEHIG.tex', 'KDE HIG Documentation',
     'KDE', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'kdehig', 'KDE HIG Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'KDEHIG', 'KDE HIG Documentation',
     author, 'KDEHIG', 'One line description of project.',
     'Miscellaneous'),
]

# Adding common substitions between Kirigami and HIG
from epilog import rst_epilog

# Adding global substitutions
rst_epilog += """
.. |devicon| image:: /img/DevIcon.svg
             :width: 32px
             :height: 32px

.. |designicon| image:: /img/DesignerIcon.svg
                :width: 32px
                :height: 32px

.. |touchicon| image:: /img/transform-browse.svg
                :width: 32px
                :height: 32px
                
.. |desktopicon| image:: /img/computer.svg
             :width: 32px
             :height: 32px

.. |mobileicon| image:: /img/smartphone.svg
             :width: 32px
             :height: 32px


.. |br| raw:: html

   <br />

.. |nbsp| raw:: html

   &#160;

"""

doxylink = {
    'kirigamiapi' : ('Kirigami2.tags', 'https://api.kde.org/frameworks/kirigami/html/'), # https://api.kde.org/frameworks/kirigami/html/Kirigami2.tags
    'kwidgetsaddonsapi' : ('KWidgetsAddons.tags', 'https://api.kde.org/frameworks/kwidgetsaddons/html/'), # https://api.kde.org/frameworks/kwidgetsaddons/html/KWidgetsAddons.tags
    'plasmaapi' : ('Plasma.tags', 'https://api.kde.org/frameworks/plasma-framework/html/') # https://api.kde.org/frameworks/plasma-framework/html/Plasma.tags
}

for doc in doxylink.values():
    print(bold("Downloading file {} to {}".format(doc[1] + "/" + doc[0], doc[0])))
    tagFile = open("../" + doc[0], "w")
    tagFile.write(requests.get(doc[1] + "/" + doc[0]).text)
    tagFile.close()


rst_prolog = """
.. role:: iconred
.. role:: plasmablue
.. role:: noblefir
.. role:: intend
"""

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'kirigami': ('https://kirigami.kde.org/', None),
    'pm': ('https://docs.plasma-mobile.org', None)
}

# add css file
def setup(app):
    app.add_stylesheet('https://cdn.kde.org/aether-devel/sphinx-doc.css')
    app.add_javascript('js/custom.js')
