
author = 'Your Name'
release = ''


extensions = []

exclude_patterns = []


html_static_path = ['_static']
html_css_files = ['custom.css']
html_sidebars = {'**': []}
html_title = ""
html_js_files = ['hide-version.js']
templates_path = ['_templates']
import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_js_files = ['remove-flyout.js']


