SUMMARY = "EdgeDev Lab 5 Image"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

inherit core-image

SYSTEM_UTILS = " \
    nano \
    usbutils \
    pciutils \
    screen \
"

NETWORK_UTILS = " \
    nmap \
"

PYTHON3_INSTALL = " \
    python3 \
    python3-paho-mqtt \
    python3-pyftdi \
    python3-luma-core \
    python3-luma-oled \
    python3-pimoroni-bme280 \
    python3-pyfiglet \
    python3-boto3 \
"

IMAGE_INSTALL = " \
    packagegroup-core-boot \
    hello \
    webserver-demo \
    webapi-demo \
    sensor-board-demo \
    lab5-driver-example \
    system-ambient-temp \
    system-ambient-temp-service \ 
    lab4-project-v2 \
    lab4-project-v2-service \
    ${SYSTEM_UTILS} \
    ${NETWORK_UTILS} \
    ${PYTHON3_INSTALL} \
    ${CORE_IMAGE_EXTRA_INSTALL} \
"

IMAGE_FEATURES_append = " \
    ssh-server-openssh \
"

DISTRO_FEATURES_append = " systemd"
DISTRO_FEATURES_BACKFILL_CONSIDERED += "sysvinit"
VIRTUAL-RUNTIME_init_manager = "systemd"
VIRTUAL-RUNTIME_initscripts = "systemd-compat-units"

IMAGE_LINGUAS = " "

IMAGE_ROOTFS_SIZE ?= "8192"
IMAGE_ROOTFS_EXTRA_SPACE_append = "${@bb.utils.contains("DISTRO_FEATURES", "systemd", " + 4096", "" ,d)}"
