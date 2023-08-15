## Requirements

* [Python 3](https://www.python.org/downloads/)
* [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html)

You can install [Cookiecutter Python package](https://cookiecutter.readthedocs.io/en/latest/installation.html) easily with conda.

``` bash
pip install --user cookiecutter
```

## Not required but highly recommended
	@@ -25,7 +25,7 @@ conda install -c conda-forge cookiecutter
To start a new project, run:

``` bash
cookiecutter gh:/ValentinGuigon/cookiecutter-neuro-research-project
```

(*this should be run from the location that you want the project folder to live, or you will need to move the directory around later*)
	@@ -54,6 +54,8 @@ git init

We now want to connect this local repository to a github repo. This can be done directly from the command line using the [Github Command Line Interface](https://github.com/cli/cli#installation). You will have to install it following one of the methods described [here](https://github.com/cli/cli#installation)


### Outdated method (for MacOSx)
**Note**: if you do not have sudo privileges for your machine, it may be more straightforward to manually initialize a repo on GitHub with the _exact same name_ as your project, and then link this with your local project repo. See [here](https://docs.github.com/en/github/importing-your-projects-to-github/importing-source-code-to-github/adding-an-existing-project-to-github-using-the-command-line) for a description of how to do this.

If using the Github Command Line Interface, simply navigate to the project root folder and type:


## Important to use cookiecutter when R is part of the script:
**In hooks/post_gen_project.py, make sure you change line 36 to suit your situation**:
* On Mac/Linux, the Rscript path is typically /usr/local/bin/Rscript or /usr/bin/Rscript.
* On Windows, the path for R version X.Y.Z is typically C:/Program Files/R/R-X.Y.Z/bin/Rscript.exe

## Important to use cookiecutter when MATLAB is part of the script:
* The block that uses octave requires octave GNU installed, on path and working
* The block that uses matlab engine requires to call the appropriate python version by first setting up an install
* If no solution work, execute `init/init.m` by hand