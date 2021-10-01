# Cookiecutter Research Project

A lightweight cookiecutter template for a research project in python (perhaps with some MATLAB too).

This borrows heavily from [cookiecutter-data-science](https://drivendata.github.io/cookiecutter-data-science/), [cookiecutter-science-project](https://github.com/jbusecke/cookiecutter-science-project) and [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage). However, it avoids testing frameworks, CI and documentation generation in an effort to keep things simple. 

## Requirements

* [Conda package manager](https://conda.io/en/latest/) (I recommend the lightweight version [miniconda](https://docs.conda.io/en/latest/miniconda.html))
* [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html)

You can install [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) easily with conda.

``` bash
conda install -c conda-forge cookiecutter
```

## Not required but highly recommended

* A [github](https://github.com/) account.
    * Note that everything is easier if you set up [authentication via SSH key-pair](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh).

## Quickstart

To start a new project, run:

``` bash
cookiecutter gh:jessecusack/cookiecutter-research-project
```

(*this should be run from the location that you want the project folder to live, or you will need to move the directory around later*)

If you have previously created a package with this template confirm the prompt to redownload the newest version.
The installation dialog will ask for a few inputs:
* `full_name`: Your name.
* `email`: Your email.
* `project_name`: The name of the project which is also the name of the directory if will be created in (whitespaces will be replaced with underscores).
* `description`: A short description of the project for the readme.
* `conda_environment_name`: The desired name of the conda environment associated with the project. This defaults to the project name.
* `as_python_package`: Answering yes will add the basic configuration files and folders (`setup.cfg`, `pyproject.toml`, etc.) to install your project as a python package.
* `include_matlab`: To include a `matlab_toolboxes/` directory.
* `create_author_file`: To include an `AUTHOR.md` file. 
* `open_source_license`: Choose a license for your project.

> Unfortunately there seems to be a bug that does [not allow backspace](https://github.com/audreyr/cookiecutter/issues/875) in cookiecutter on certain platforms. If you make a typo cancel the input `ctrl+c` and start over again.

### Setting up git/github

To initialize a git repository in the folder, navigate to your project folder that was just created and do

```bash
git init
```

We now want to connect this local repository to a github repo. This can be done directly from the command line using the [Github Command Line Interface](https://github.com/cli/cli#installation). You will have to install it following one of the methods described [here](https://github.com/cli/cli#installation)

**Note**: if you do not have sudo privileges for your machine, it may be more straightforward to manually initialize a repo on GitHub with the _exact same name_ as your project, and then link this with your local project repo. See [here](https://docs.github.com/en/github/importing-your-projects-to-github/importing-source-code-to-github/adding-an-existing-project-to-github-using-the-command-line) for a description of how to do this.

If using the Github Command Line Interface, simply navigate to the project root folder and type:

```bash
gh repo create 
```
and follow the instructions. You might have to authenticate this if you are using it for the first time, but this should all be explained by prompts in the command line. 

Now all you need to do is commit the files and push them (the remote has already been set by the previous command).
