#!/bin/bash

# Define variables
repo_url="http://digital-hands-furuqw@git.codesubmit.io/digital-hands/etl-munqup"
password="B+AXx6TcJ"

# Clone the repository with the provided URL and password
git clone $repo_url

# If the repository requires authentication, set the password
cd etl-munqup
git config --local credential.helper '!f() { echo "username=digital-hands-furuqw"; echo "password=$password"; }; f'

# Pull changes to ensure the latest version is obtained
git pull
