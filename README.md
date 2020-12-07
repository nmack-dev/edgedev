# edgedev
This repository aims to showcase my labs/projects from the IoT Edge Development class at Case Western Reserve University. The majority of projects run on a custom Intel DE2i-150 Board. This board has an Atom Processor, FPGA, and lots of different I/O. As we complete projects in this course, I will update this repository.

## Lab 1
The purpose of lab 1 was to serve as a gentle introduction to embedded systems and IoT devices. Using a small microcontroller and OLED screen, we wrote a custom program to interface with the OLED screen over I2C. The program moving_cube.py displays a cube that moves from left to right and then down one level.

## Lab 2
The purpose of lab 2 was to teach us about MQTT, data dashboards, and Linux daemon scripts. The program sensor_datalogger.py pulls data from a BME280 climate sensor and feeds it to a microcontroller over I2C. The microcontroller then sends that data over to an OLED screen to be displayed. The program also sends the BME280 data to an MQTT broker for collection. The script, datalogger_daemon.sh, runs sensor_datalogger.py on startup so that it is always collecting data.

## Lab 3
Lab3 involved us building a custom Linux image with Yocto Project and Openembedded. This image is explicitly configured for the previously mentioned Intel board and allows us to load programs and libraries onto the board.

## Lab 4
Lab 4 involved us learning about webservers and REST APIs. For my project, I created a rudimentary web server that displays climate data for the Cleveland area that updates at the click of a button. This code ran on an intel running a custom Linux image we made with yocto project and openembedded.

## Lab 5
Lab 5 involved us updated our Lab 4 and Lab 2 projects to use Systemd services on our custom Linux image. Systemd allows our programs to run by themselves on system boot. It's also an easier alternative to shell scripting when trying to accomplish this specific task. 

## Lab 6
Lab 6 focuses on learning Qt5 for embedded applications. Given the Intel board and an external screen attached to it, we were tasked with writing a Qt app to display the said screen information. My project was an app that grabs stock data off the web and shows a stock graph on the screen. The user can input their selected stock via the screen or an online web page.

## Lab 7
For lab 7, we implemented a data processing algorithm. My project involved using the Fast Fourier Transform to process guitar audio to determine what chords it contains. The user can upload a sound file to a web page, and then a web server returns the given chords of that audio. This entire system exists on the Intel board.

## Lab 8 (Final Project)
For my final project, I designed an IoT system that monitors senior citizens' fall status in assisted living facilities. If a person falls, this system knows asap, and caretakers can respond quicker. This system is specifically useful if someone is knocked out due to a fall and sustains head damage. All of this happens with a belt that contains an accelerometer sensor. See below for a system diagram. 

https://github.com/nmack-dev/edgedev/blob/master/397%20Final%20Project.png

To prototype this system, I wrote a program that simulates accelerometer data that is somewhat realistic. This data is then sent over MQTT to a broker server. From there, a program running on the Intel board acts as an MQTT client and receives that data to upload to an AWS DynamoDB. Once the data is within the DynamoDB, an AWS Lambda function is triggered to process the data to determine whether a fall has occurred. The result, along with other identification information, is stored in another DynamoDB. A webserver running on the Intel board collects data from the first DynamoDB to display on a dashboard. A Qt app running on the Intel board pulls data from the second DynamoDB to indicate when an individual has fallen.

A future implementation is to use AWS SNS within the Lamda function to notify caretakers over text when a fall has occurred. 

