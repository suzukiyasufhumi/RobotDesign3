#!/bin/bash -exv

sudo apt-get install apache2
sudo cp ./apache2.conf /etc/apache2/sites-available/default
sudo service apache2 restart
sudo make install
