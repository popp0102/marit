# README
MARIT - MAC Address Randomization Identification Tool

# Setup

## Setup Ruby App
1. Install ruby 2.7.5
2. bundle install
3. bundle exec rake db:drop
4. bundle exec rake db:setup

## Setup Python Env
1. Install pip
2. Install python 3.6.3
3. Install pytz, datetime, scapy, argparse, and sqlite3 through pip

## Setup Network Card
1. Change your network card into "monitor mode" (note not all cards can do this)
2. Ensure your network is capable of packet injection

## Running the project
1. sudo ./bin/rails server
2. open a browser
3. localhost:3000

