#!/bin/bash

# Clone the prod ADF repo
git config --global user.email "calebadeyemi@gmail.com"
git config --global user.name "Caleb Adeyemi"

eval `ssh-agent -s`

rm -rf adf_cicd/
git clone https://github.com/calebu/adf_cicd.git
ls adf_cicd/
git clone https://github.com/calebu/adf_qa.git
cd adf_qa
rm -rf ../adf_cicd/.git*
cp -r ../adf_cicd/* .
#rm -rf adf_cicd/

# Push to lower environment

chmod 400 ./key_rsa && SSH_ASKPASS=/path/to/ssh_give_pass.sh ssh-add ./key_rsa <<< "what"
git remote set-url origin git@github.com:calebu/adf_qa.git
git add .
git commit -m "Pushing latest commit in Prod to lower environments"

git push
#git push --repo https:/github.com/calebu/adf_qa_.git

