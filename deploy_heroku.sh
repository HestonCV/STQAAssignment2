#!/bin/bash

heroku git:remote -a bmi-calculator-heston

echo "Setting up Heroku git authentication..."
git config --global user.email "heston.cv@gmail.com"
git config --global user.name "Heston Vaughan"
echo "machine git.heroku.com login apikey password $HEROKU_API_KEY" > ~/.netrc
chmod 600 ~/.netrc

echo "Deploying to Heroku..."
git push heroku main:master


