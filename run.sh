#!/bin/bash

# build jupyter notebook

docker build -t jupyterlab:jupyterlab ./images/jupyterlab


docker run -p 8888:8888 --name jupyterlab -v .:/app -t jupyterlab:jupyterlab