#!/bin/bash

# Set Heroku remote
heroku git:remote -a bmi-calculator-heston

# Authenticate for git operations
echo "Setting up Heroku git authentication..."
git config --global user.email "heston.cv@gmail.com"  # Replace with your email
git config --global user.name "Heston Vaughan"  # Replace with your name
echo "machine git.heroku.com login apikey password $HEROKU_API_KEY" > ~/.netrc
chmod 600 ~/.netrc

# Push to Heroku
echo "Deploying to Heroku..."
git push heroku main:master

# Replace `main` with your branch name if it's not `main`.
