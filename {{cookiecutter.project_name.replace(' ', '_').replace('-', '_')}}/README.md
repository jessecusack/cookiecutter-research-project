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

---
{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
{% endif %}