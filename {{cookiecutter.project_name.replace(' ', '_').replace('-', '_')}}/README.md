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
This structure is adapted from the TIER protocol 4.0 (https://www.projecttier.org/tier-protocol/protocol-4-0/root/).
Each folder and subfolder has to have a descriptive and meaningful name, contains the files that are supposed to be in there, and a readme file documents the content of each.
{% set dir_name = cookiecutter.project_name.replace(' ', '_').replace('-', '_') -%}

```
{{dir_name}}/
    ├── LICENSE
    ├── README.md          <- The top-level README for people using this project.
{%- if cookiecutter.create_author_file == 'y' %}
    ├── AUTHORS.md         <- Author information.
{%- endif %}
    ├── data/
    │   ├── raw            <- Data files you initially obtain or construct at the beginning of your project.
    │   ├── processed      <- Data that you have cleaned and processed.
    │   ├── intermediate   <- Data created at some point in the processing of your data that need to be saved temporarily.
    │   └── README.md      <- Information on data sources and retrieval. 
    │
    ├── scripts/           <- Jupyter notebooks, MATLAB code and anything else that constitutes analysis.
    │   ├── processing     <- Scripts that transform raw data files into processed data files.
    │   ├── analysis       <- Scripts that produce the results, such as figures, tables and statistics.
    │   ├── supplementary  <- Scripts that produce the results present in the Supplementary Materials.
    │   ├── README.md      <- Any information about the analysis, such as execution order. 
    │   ├── *.py           <- Master script in Python that reproduces the Results of your project by executing all the other scripts, in the correct order.
    │   ├── *.m            <- Master script in MATLAB that reproduces the Results of your project by executing all the other scripts, in the correct order.
    │   └── *.r            <- Master script in in R that reproduces the Results of your project by executing all the other scripts, in the correct order.
    │
    ├── output/            <- Saved figures, tables and other outputs generated during analysis.
    │   ├── results        <- Contains files presented in your report.
    │   ├── supplementary  <- Contains files presented in the Supplementary Materials.
    │   └── README.md      <- Information on data outputs and about scripts that produce them. 
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
