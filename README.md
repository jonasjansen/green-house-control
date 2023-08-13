# green-house-control

## Description

This project is a simple green house control system. 
It was the capstone project for the Internet of Things Course at the UIUC.
There are three subfolders in this repository:
- `green-house-app`: This folder contains the code for an iOS app that can be used to control the green house system.
- `green-house-raspi`: This folder contains the code for the green house system.
- `green-house-sprout-detect`: This folder contains the code for training a model to detect sprouts.


## Green House System

The green house system is a simple system that can be used to control the temperature and humidity of a green house.
The system is composed of a Raspberry Pi, a temperature and humidity sensor, a fan, a heater, and a humidifier.
The Raspberry Pi is connected to the temperature and humidity sensor, the fan, the heater, and the humidifier.
Further, the Raspberry Pi is connected to a camera module.

The app can be used to watch the temperature and humidity of the green house and manually control the fan, heater, and humidifier.
Also, the current image of the green house can be viewed in the app.
The communication between app and green house system is done via google firebase.

The taken images are were used to train a model to detect sprouts with tensorflow.
The model the used to detect sprouts in the images taken by the camera module. The result can be seen in the app, too.
