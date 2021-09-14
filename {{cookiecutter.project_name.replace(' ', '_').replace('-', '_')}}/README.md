{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name.replace('-', ' ').replace('_', ' ').title() }}

{{ cookiecutter.description }}

## Requirements

* [Conda package manager](https://conda.io/en/latest/) (I recommend the lightweight version [miniconda](https://docs.conda.io/en/latest/miniconda.html))

## Installing and removing the environment

A conda environment is specified in `environment.yml` and may be install using the appropriate bash scripts. 

To install:

```bash
./install_environment.sh
```

To remove:

```bash
./remove_environment.sh
```

These also install/remove the jupyter kernel for the environment.

> If these don't execute, you might need to change the file permissions with `chmod u+x *.sh`.

## Project Structure
{% set dir_name = cookiecutter.project_name.replace(' ', '_').replace('-', '_') -%}

```
{{dir_name}}/
    ├── LICENSE
    ├── README.md          <- The top-level README for people using this project.
{%- if cookiecutter.create_author_file == 'y' %}
    ├── AUTHORS.md         <- Author information.
{%- endif %}
    ├── data/
    │   ├── external       <- Data pulled in from outside of this project.
    │   ├── internal       <- Data generated within this project.
    │   └── README.md      <- Information on data sources and retrieval. 
    │
    ├── analysis/          <- Jupyter notebooks, MATLAB code and anything else that constitutes analysis.
    │   ├── README.md      <- Any information about the analysis, such as execution order. 
    │   ├── *.py           <- Python files that can be converted to notebooks using jupytext.
    │   └── *.m            <- Analysis in MATLAB.
    │
    ├── figures/           <- Saved figures generated during analysis.
    │
    ├── environment.yml    <- Conda environment specification. Install using the bash scripts.
{%- if cookiecutter.as_python_package == 'y' %}
    │
    ├── setup.cfg          <- Makes project pip installable (pip install -e .) so that modules 
    │                         can be imported by scripts in the analysis directory.
    ├── pyproject.toml     <- Also required for python installation.
    ├── {{dir_name}}/
    │   ├── __init__.py    <- Makes {{dir_name}} a Python package.
    │   └── module.py      <- A Python module.
{%- endif %}
{%- if cookiecutter.include_matlab == 'y' %}
    │
    ├── matlab_toolboxes/  <- A place for 3rd party MATLAB toolboxes.
    │   ├── toolbox/
    │   │
    │   └── get_toolbox.sh <- Script to download toolboxes.
{%- endif %}
 ```

---
{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
{% endif %}
