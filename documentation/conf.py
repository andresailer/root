import logging
import os
import subprocess

subprocess.call('conda list', shell=True)

subprocess.call('env', shell=True)

os.environ["CPATH"] = os.path.join(os.environ["CONDA_ENVS_PATH"], os.environ["CONDA_DEFAULT_ENV"], "usr/include")

subprocess.call('cd doxygen ; make', shell=True)

html_extra_path = ['../build/html']
