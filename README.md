# ROS Prometheus

## Overview

This repository aims to push ROS message to a Prometheus server via Python.
This repository will contain scripts to create a Prometheus Server as well.

## Requirements

The following are required to implement this application

  - Python
  - ROS

## Development

26 January - Creation of repository as well as preliminary planning
30 January - Added LoRa RSSI script, README instructions, etc. 

## How to Use

  In a terminal run the ff:

  - roscore

  In a new terminal run:

  - rosrun rosserial_python serial_node.py /dev/ttyACM0

  In a new terminal run:

  - rosrun rosserial_python serial_node.py /dev/ttyACM1 __name:=nodeRX

  In a new terminal run the pkg script:

  - rosrun ros_prometheus rssi_prometheus.py

  In a new terminal start the prometheus server.

  - ./prometheus --web.listen-address="<IP of machine>:<port>"

  The default port is 9090. If you change the port make sure to add that as a datasource.

## How to kill port in Ubuntu

  In terminal run the ff:
    
  - sudo kill -9 `` ` `` sudo lsof -t -i:XXXX`` ` ``

  Where XXXX is the port number. Mind the back ticks.

## How to edit the Prometheus server to scrape a target port.

  In the prometheus.yml file edit the scrape_configs, static_configs.
  Add the target port

  - - targets: ["<IP of machine>:<port>"]
  
