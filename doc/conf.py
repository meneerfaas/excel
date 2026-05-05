import os
import sys
from pathlib import Path

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Werken met Excel'
copyright = '2026, S. Faas'
author = 'S. Faas'
release = '0.1'
language = 'nl'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_design',
              'myst_parser',
              'sphinxcontrib.plantuml',
              'sphinx_new_tab_link']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_theme_options = {
    "logo": {
        "text": "Werken met Excel",
        "alt_text": "Werken met Excel",
        "image_light": "images/excel_128.png",
        "image_dark": "images/excel_128.png",
    },
    "footer_start": ["sphinx-version"],
    "footer_center": ["copyright"],
    "footer_end": ["theme-version"]
}
html_favicon = "_static/favicon.png"

# -- Options for plantuml
local_plantuml_path = os.path.join(os.path.dirname(
    __file__), "utils", "plantuml.jar")
plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
plantuml_output_format = 'svg'
