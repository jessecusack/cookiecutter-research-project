from glob import glob
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.append("/init")

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if not '{{cookiecutter.include_python}}' == 'yes':
    remove('init/__init__.py')

if not '{{cookiecutter.include_matlab}}' == 'yes':
    remove('matlab_toolboxes')
    remove('init/init.m')

if not '{{cookiecutter.include_r}}' == 'yes':
    remove('output/R_environments')
    remove('init/init.R')

if not '{{cookiecutter.include_python}}' == 'yes' and not '{{cookiecutter.include_matlab}}' == 'yes' and not '{{cookiecutter.include_r}}' == 'yes':
    remove('init/')

    
if not '{{cookiecutter.create_author_file}}' == 'yes':
    remove('AUTHORS.md')
    
if '{{ cookiecutter.open_source_license }}' == 'Not open source':
    remove('LICENSE')

if '{{cookiecutter.include_r}}' == 'yes':
    command = 'C:/Program Files/R/R-4.3.1/bin/x64/Rscript'
    arg = '--vanilla' 
    subprocess.call([command, arg, "init/init.R"], shell=True)

''' uses octave
if '{{cookiecutter.include_matlab}}' == 'yes':
    from oct2py import Oct2Py
    path = Path('.')
    octave.addpath(octave.genpath('path/init')) 
    octave.savepath() 
    octave.run('init.m')
'''
''' uses matlab engine, 
see https://fr.mathworks.com/matlabcentral/answers/553642-how-do-i-chose-the-correct-version-of-python-when-trying-to-install-the-matlab-engine-api
if '{{cookiecutter.include_matlab}}' == 'yes':
    import matlab.engine
    eng = matlab.engine.start_matlab()
    eng.addpath(init)
    eng.init(nargout=0)
'''

# Make the shell scripts executable
for sh_script in glob("*.sh"):
    os.chmod(sh_script, 0o744)