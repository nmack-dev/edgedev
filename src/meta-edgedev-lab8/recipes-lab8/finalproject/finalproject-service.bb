SUMMARY = "Final Project Systemd Service"
SECTION = "examples"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

RDEPENDS_${PN} = "finalproject"

SRC_URI = " \
  file://localdash.service \
  file://recieve_node_data.service \
  file://server.service \
"

S = "${WORKDIR}"

inherit systemd

SYSTEMD_SERVICE_${PN} = " \ 
  localdash.service \
  recieve_node_data.service \
  server.service \
"

do_install() {
  install -d ${D}${systemd_system_unitdir}
  install -m 0644 ${S}/localdash.service ${D}${systemd_system_unitdir}/localdash.service
  install -m 0644 ${S}/recieve_node_data.service ${D}${systemd_system_unitdir}/recieve_node_data.service
  install -m 0644 ${S}/server.service ${D}${systemd_system_unitdir}/server.service
}

FILES_${PN} = " \
  ${systemd_system_unitdir}/localdash.service \
  ${systemd_system_unitdir}/recieve_node_data.service \
  ${systemd_system_unitdir}/server.service \
"

REQUIRED_DISTRO_FEATURES = "systemd"