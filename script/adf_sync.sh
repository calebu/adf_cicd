#!/bin/bash

# Clone the prod ADF repo
git config --global user.email "calebadeyemi@gmail.com"
git config --global user.name "Caleb Adeyemi"
echo $1
#eval `ssh-agent -s`
#chmod 400 ./key_rsa
#ssh-add ./key_rsa
cd adf_qa
git clone https://github.com/calebu/adf_cicd.git
rm -rf adf_cicd/.git*
cp -r adf_cicd/* .
# Push to lower environment
git add .
git commit -m "Pushing latest commit in Prod to lower environments"
#git push --repo https://calebu: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@github.com/calebu/adf_qa_.git

#git remote set-url origin https://github.com/calebu/adf_qa.git
#git push -u origin master
#git branch --set-upstream-to https://github.com/calebu/adf_qa.git
#git push -u origin main
