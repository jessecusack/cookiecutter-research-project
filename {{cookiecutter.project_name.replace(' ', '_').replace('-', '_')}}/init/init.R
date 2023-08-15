#! /usr/bin/Rscript

# load packages usethis and here
list.of.packages=c("usethis", "here")
{
  new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
  if(length(new.packages)) install.packages(new.packages)
  lapply(list.of.packages, require, character.only = TRUE)
}

# find current folder to locate parent folder (i.e., root) bearing the name of the project
currentFolder = here::here()
project_name = basename(normalizePath(file.path(currentFolder)))
project_path = normalizePath(file.path(currentFolder))
setwd(project_path)

# create a new Rproj
create_project(path = '.', open = FALSE, rstudio = TRUE)

# load package renv
list.of.packages2=c("renv")
{
  new.packages <- list.of.packages2[!(list.of.packages2 %in% installed.packages()[,"Package"])]
  if(length(new.packages)) install.packages(new.packages)
  lapply(list.of.packages2, require, character.only = TRUE)
}

renv::init()
