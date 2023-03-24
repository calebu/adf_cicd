#!/bin/bash

# Clone the prod ADF repo
git config --global user.email "calebadeyemi@gmail.com"
git config --global user.name "Caleb Adeyemi"

eval `ssh-agent -s`
chmod 400 ./key_rsa
git clone https://github.com/calebu/adf_qa.git
cd adf_qa
git clone https://github.com/calebu/adf_cicd.git
rm -rf adf_cicd/.git*
cp -r adf_cicd/* .
rm -rf adf_cicd/
# Push to lower environment
ssh-add ./key_rsa
git remote set-url origin git@github.com:calebu/adf_qa.git
git add .
git commit -m "Pushing latest commit in Prod to lower environments"

#git push --repo https:/github.com/calebu/adf_qa_.git
git push

#git remote set-url origin https://github.com/calebu/adf_qa.git
#git push -u origin master
#git branch --set-upstream-to https://github.com/calebu/adf_qa.git
#git push -u origin main
