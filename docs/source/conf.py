



# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'RLforQT'

author = 'Xyg'

release = '0.1'
version = '0.1.0'

# -- General configuration

# extensions = [
#     'sphinx.ext.autodoc',
#     'sphinx.ext.viewcode',
# ]

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx-markdown-tables',
#     'recommonmark', 
    'myst_parser',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'pip': ("https://pip.pypa.io/en/stable/", None),
    'myst-parser': ("https://myst-parser.readthedocs.io/en/stable/", None),
    'sphinx-markdown-tables':("https://pypi.org/project/sphinx-markdown-tables/",None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
source_suffix= '.md'
# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.md': 'markdown',
# }

master_doc = 'index'

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
