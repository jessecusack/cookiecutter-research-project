from glob import glob
import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if not '{{cookiecutter.as_python_package}}' == 'y':
    remove('{{cookiecutter.project_name.replace(' ', '_').replace('-', '_')}}')
    remove('pyproject.toml')
    remove('setup.cfg')

if not '{{cookiecutter.include_matlab}}' == 'y':
    remove('matlab_toolboxes')
    
if not '{{cookiecutter.create_author_file}}' == 'y':
    remove('AUTHORS.md')
    
if '{{ cookiecutter.open_source_license }}' == 'Not open source':
    remove('LICENSE')
    
# Make the shell scripts executable
for sh_script in glob("*.sh"):
    os.chmod(sh_script, 0o744)