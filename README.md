# edgedev
The purpose of this repository is to showcase my labs/projects from the IoT Edge Development class at Case Western Reserve University. The majority of projects are run on a custom Intel DE2i-150 Board. This board is equiped with an Atom Processor, FPGA, and lots of different I/O. As we complete projects in this course, I will update this repository.

## Lab 1
The purpose of lab 1 was to serve as a soft introduction to embedded systems and IoT devices. Using a small micocontroller and OLED screen, we wrote a custom program to interface with the OLED screen over I2C. The program moving_cube.py displays a cube that moves from left to right and then down one level.

## Lab 2
The purpose of lab 2 was to teach us about MQTT, data dashboards, and linux daemon scripts. The program sensor_datalogger.py pulls data from a BME280 climate sensor and feeds it to a microcontroller over I2C. The microcontroller then sends that data over to an OLED screen to be displayed. The program also sends the BME280 data to an MQTT broker for collection. The script, datalogger_daemon.sh, runs sensor_datalogger.py on startup so that it is always collecting data.

## Lab 3
Lab3 involved us building a custom linux image with yocto project and openembedded. This image is configured specifically for the previously mentioned Intel board, and allows us to load programs and libraries onto the board.

## Lab 4
Lab 4 involved us learning about webservers and REST APIs. For my project, I created a rudimentary webserver that displays climate data for the Cleveland area that updates at the click of a button. All of this code was running on an intel running a custom linux image we made with yocto project and openembedded.

## Lab 5
Lab 5 involved us updated our Lab 4 and Lab 2 projects to use systemd services on our custom linux image. Systemd allows our programs to run by themselves on system boot. It's also an easier alternative to shell scripting when trying to accomplish this specific task. 

## Lab 6
Lab 6 was focused on learning Qt5 for embedded applications. Given the Intel board and an external sceen attached to it, we were tasked with writing a Qt app to display information on said screen. My project was an app that grabs stock data off the web and displays a graph of that stock on the screen. The user can input their selected stock via the screen or an online web page.

## Lab 7
For lab 7, we were tasked to implement a data processing algorithm. My project involved using the Fast Fourier Transform to process guitar audio in order to determine what chords the audio consists of. The user is able to upload a sound file to a web page, and then a web server returns the given chords of that audio. This entire system was loaded onto the Intel board.

## Lab 8 (Final Project)
For my final project, I designed an IoT system that monitors the fall status of senior citizens in assisted living facilities. If a senior falls, this system is notified asap, and caretakers can respond quicker. This system is specifically useful if someone is knocked out due to a fall and sustains head damage. See below for a system diagram. 



