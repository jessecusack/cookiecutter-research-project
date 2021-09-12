# Cookiecutter Research Project

A bare-bones cookiecutter for a research project in python and/or MATLAB.

## Requirements

* [Conda package manager](https://conda.io/en/latest/) (I recommend the lightweight version [miniconda](https://docs.conda.io/en/latest/miniconda.html))
* [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html)

You can install [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) easily with conda.

``` bash
$ conda install -c conda-forge cookiecutter
```

## Quickstart

To start a new project, run:

``` bash
$ cookiecutter gh:jessecusack/cookiecutter-research-project
```

(*this should be run from the location that you want the project folder to live, or you will need to move the directory around later*)

If you have previously created a package with this template confirm the prompt to redownload the newest version.
The installation dialog will ask for a few inputs:
* `full_name`: Your name.
* `email`: Your email.
* `project_name`: The name of the project (whitespaces will be replaced with underscores).
* `project_short_description`: A short description of the project for the readme.
* `conda_environment_name`: The desired name of the conda environment associated with the project. This defaults to the project name. 
* `create_matlab_toolboxes_directory`: Answering yes to this prompt will cause a directory to be generated for matlab_toolboxes. 
* `open_source_license`: Chose a license for your package.

> Unfortunately there seems to be a bug that does [not allow backspace](https://github.com/audreyr/cookiecutter/issues/875) in cookiecutter on certain platforms. If you make a typo cancel the input `ctrl+c` and start over again.