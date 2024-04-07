#!/bin/bash

# Authenticate with Heroku
echo "Logging into Heroku..."
heroku login --api-key $HEROKU_API_KEY

# Set Heroku remote
heroku git:remote -a bmi-calculator-heston

# Push to Heroku
echo "Deploying to Heroku..."
git push heroku main:master