SUMMARY = "BME280 Systemd Service"
SECTION = "examples"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

RDEPENDS_${PN} = "sensor-board-demo"

SRC_URI = "file://read-bme280.service"

S = "${WORKDIR}"

inherit systemd

SYSTEMD_SERVICE_${PN} = "read-bme280.service"

do_install() {
  install -d ${D}${systemd_system_unitdir}
  install -m 0644 ${S}/read-bme280.service ${D}${systemd_system_unitdir}/read-bme280.service
}

FILES_${PN} = "${systemd_system_unitdir}/read-bme280.service"

REQUIRED_DISTRO_FEATURES = "systemd"