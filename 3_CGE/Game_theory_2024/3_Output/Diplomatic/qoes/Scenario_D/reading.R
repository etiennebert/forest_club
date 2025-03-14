

install.packages('devtools')
devtools::install_git('https://github.com/USDA-ERS/MTED-HARr.git')
install.packages("readxl")
install.packages("xlsx", dependencies=TRUE)
install.packages("rJava")
install.packages("xlsx")

#clear the environment
rm(list = ls())

## Run these lines in each new R session where you need these packages
library(devtools)
library(xlsx)
require(HARr)
library("readxl")
library("rstudioapi")
library(dplyr)
library(writexl)
library(tidyr)


data = read_SL4('NATDEF_4.sl4')