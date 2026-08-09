project = "ztachip"
author = "ztachip project"
copyright = "ztachip contributors"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_title = "ztachip Documentation"
html_logo = None
html_show_sphinx = False
html_show_sourcelink = True

html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "includehidden": True,
    "titles_only": False,
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "substitution",
    "tasklist",
]

myst_heading_anchors = 4
