#!/bin/bash

# Clone the prod ADF repo
git config --global user.email "calebadeyemi@gmail.com"
git config --global user.name "Caleb Adeyemi"

#eval `ssh-agent -s`

rm -rf adf_cicd/
git clone https://github.com/calebu/adf_cicd.git
git clone https://github.com/calebu/adf_qa.git
cd adf_qa
rm -rf ../adf_cicd/.git*
rm -rf ../adf_cicd/script
rm -rf ../adf_cicd/*.sh
cp -r ../adf_cicd/* .

# Push to lower environment
# Private key needs to be present in key_rsa file, and added to the destination git repo

chmod 400 ./key_rsa && SSH_ASKPASS=/path/to/ssh_give_pass.sh ssh-add ./key_rsa <<< $1
git remote set-url origin git@github.com:calebu/adf_qa.git
git add .
git commit -m "Pushing latest commit in Prod to lower environments"

git push
