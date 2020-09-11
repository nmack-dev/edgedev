# edgedev
The purpose of this repository is to showcase my labs/projects from the IoT Edge Development class at Case Western Reserve University. The majority of projects are run on a custom Intel DE2i-150 Board. This board is equiped with an Atom Processor, FPGA, and lots of different I/O. As we complete projects in this course, I will update this repository.

## Lab 1
The purpose of lab 1 was to serve as a soft introduction to embedded systems and IoT devices. Using a small micocontroller and OLED screen, we wrote a custom program to interface with the OLED screen over I2C. The program moving_cube.py displays a cube that moves from left to right and then down one level.

## Lab 2
The purpose of lab 2 was to teach us about MQTT, data dashboards, and linux daemon scripts. The program sensor_datalogger.py pulls data from a BME280 climate sensor and feeds it to a microcontroller over I2C. The microcontroller then sends that data over to an OLED screen to be displayed. The program also sends the BME280 data to an MQTT broker for collection. The script, datalogger_daemon.sh, runs sensor_datalogger.py on startup so that it is always collecting data.
