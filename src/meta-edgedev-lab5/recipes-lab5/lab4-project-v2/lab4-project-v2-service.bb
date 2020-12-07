SUMMARY = "Lab 4 v2 project Systemd service"
SECTION = "examples"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

RDEPENDS_${PN} = "lab4-project-v2"

SRC_URI = "file://main.service"

S = "${WORKDIR}"

inherit systemd

SYSTEMD_SERVICE_${PN} = "main.service"

do_install() {
  install -d ${D}${systemd_system_unitdir}
  install -m 0644 ${S}/main.service ${D}${systemd_system_unitdir}/main.service
}

FILES_${PN} = "${systemd_system_unitdir}/main.service"

REQUIRED_DISTRO_FEATURES = "systemd"