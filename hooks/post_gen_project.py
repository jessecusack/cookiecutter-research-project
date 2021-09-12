from glob import glob
import os
import shutil

print(os.getcwd())

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

create_matlab_toolbox = '{{cookiecutter.create_matlab_toolboxes_directory}}' == 'y'

if not create_matlab_toolbox:
    # remove top-level folder
    remove('matlab_toolboxes')
    
# Make the shell scripts executable
for sh_script in glob("*.sh"):
    os.chmod(sh_script, 0o744)