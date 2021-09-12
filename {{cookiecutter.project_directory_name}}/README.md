{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_directory_name.replace('-', ' ').replace('_', ' ').title() }}

{{ cookiecutter.project_short_description }}

## Requirements

This project requires [`conda`](https://docs.conda.io/en/latest/miniconda.html). 

## Installing and removing the environment

A conda environment is specified in `environment.yml` and may be install using the appropriate bash scripts. 

To install:

    ./install_environment.sh
    
To remove:

    ./remove_environment.sh
    
These also create a jupyter kernel for the environment.

---
{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
{% endif %}