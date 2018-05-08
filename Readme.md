# Jupyter notebook URL telegram service

## Introduction

Jupyter lab/notebook is a great IDE - one of its best features is how it exposes hardware to other people's computers, allowing you to run something on a Raspberry Pi. Headless RPi's are still annoying, though. Wouldn't it be nice if once we power up a pi we get a telegram message with the Jupyter URL?

## How to use

The script needs to be run on startup, but after wifi is connected. 

* Edit the settings 
* Place the file at some `location` you want to. We'll put it in `/usr/`
* Run `crontab -e`
* At the bottom of the file, add `@reboot /usr/bin/python /usr/jupyter-sendme.py`
