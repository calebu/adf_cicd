#!/bin/bash

# Clone the prod ADF repo
git clone https://github.com/calebu/adf_cicd.git
git branch --set-upstream-to https://github.com/calebu/adf_qa.git
git push -u origin main
