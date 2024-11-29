import logging
import os
import subprocess


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ROOT'
copyright = '2024, ROOT Developers'
author = 'ROOT Developers'
release = 'master'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


subprocess.call('conda list', shell=True)

subprocess.call('env', shell=True)

cpath = os.path.join(os.environ["CONDA_ENVS_PATH"], os.environ["CONDA_DEFAULT_ENV"], "x86_64-conda-linux-gnu/sysroot/usr/include")

os.environ["CPATH"] = cpath

subprocess.call(f'export CPATH={cpath}; cd doxygen ; make', shell=True)

subprocess.call('ls -l', shell=True)
subprocess.call('ls -l doxygen', shell=True)
subprocess.call('ls -l doxygen/source', shell=True)
subprocess.call('find .. -name "index.html"', shell=True)

html_extra_path = ['../documentation/doxygen/rootdoc/html/']
