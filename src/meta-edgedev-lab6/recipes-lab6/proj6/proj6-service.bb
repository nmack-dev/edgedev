SUMMARY = "Lab 6 - Mini Project Systemd Service"
SECTION = "examples"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

RDEPENDS_${PN} = "proj6"

SRC_URI = " \
  file://proj6.service \
  file://webserver.service \
"

S = "${WORKDIR}"

inherit systemd

SYSTEMD_SERVICE_${PN} = " \ 
  proj6.service \
  webserver.service \
"

do_install() {
  install -d ${D}${systemd_system_unitdir}
  install -m 0644 ${S}/proj6.service ${D}${systemd_system_unitdir}/proj6.service
  install -m 0644 ${S}/webserver.service ${D}${systemd_system_unitdir}/webserver.service
}

FILES_${PN} = " \
  ${systemd_system_unitdir}/proj6.service \
  ${systemd_system_unitdir}/webserver.service \
"

REQUIRED_DISTRO_FEATURES = "systemd"