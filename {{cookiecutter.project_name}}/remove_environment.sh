#!/usr/bin/env bash
source $CONDA_PREFIX/etc/profile.d/conda.sh
conda activate {{ cookiecutter.conda_environment_name }} && jupyter kernelspec uninstall {{ cookiecutter.conda_environment_name }} && conda deactivate
conda remove --name {{ cookiecutter.conda_environment_name }} --all