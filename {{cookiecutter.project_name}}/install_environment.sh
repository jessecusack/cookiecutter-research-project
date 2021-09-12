#!/usr/bin/env bash
source $CONDA_PREFIX/etc/profile.d/conda.sh
conda env create -f environment.yml
conda activate {{ cookiecutter.conda_environment_name }} && python -m ipykernel install --user --name {{ cookiecutter.conda_environment_name }}