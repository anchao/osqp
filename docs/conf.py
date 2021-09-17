#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OSQP documentation build configuration file, created by
# sphinx-quickstart on Sat Feb 18 15:49:00 2017.
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

import sphinx_rtd_theme
import os
import subprocess
# import sys
# sys.path.insert(0, os.path.abspath('.'))

__version__ = os.environ.get('OSQP_VERSION', '0.0.0')

# An incoming version number of '0.0.0' is a placeholder for missing version information.
# In such cases, use a <blank> version to effectively avoid mentioning the version number
# in the built documentation at all.
__version__ = '' if __version__ == '0.0.0' else __version__

# Set OSQP_VERSION envvar in case subprocesses (like doxygen) need it too
os.environ['OSQP_VERSION'] = __version__

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.todo', 'sphinx.ext.mathjax', 'breathe']

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
project = 'OSQP'
copyright = '2021, Bartolomeo Stellato, Goran Banjac'
author = 'Bartolomeo Stellato, Goran Banjac'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

version = '.'.join(__version__.split('.')[:4])

# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#

html_theme_options = {
    'logo_only': True,
}


html_logo = '_static/img/logo.png'
html_favicon = "_static/img/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    # Override default css to get a larger width for local build
    def setup(app):
        app.add_css_file('css/osqp_theme.css')
else:
    html_context = {
        'css_files': [
                'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
                'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
                '_static/css/osqp_theme.css'],
    }



# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'OSQPdoc'


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
    'sphinxsetup': 'hmargin={1.5cm,1.5cm}',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'OSQP.tex', 'OSQP Documentation',
     'Bartolomeo Stellato, Goran Banjac', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'OSQP', 'OSQP Documentation',
     [author], 1)
]

# -- Options for breathe ---------------------------------------

# Generate doxygen documentation
subprocess.call('doxygen doxygen.conf', shell=True)

breathe_projects = {"osqp": "doxygen_out/xml/"}
breathe_default_project = "osqp"



# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'OSQP', 'OSQP Documentation',
     author, 'OSQP', 'One line description of project.',
     'Miscellaneous'),
]
