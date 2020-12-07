SUMMARY = "Final Project for ECSE 397"
SECTION = "examples"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = " \
  file://aws_get.py \
  file://localdash.py \
  file://recieve_node_data.py \
  file://server.py \
  file://dashboard.json \
"

S = "${WORKDIR}"

install_dir = "/home/root/finalProject"

do_install() {
  install -d ${D}${install_dir}
  install -m 0755 aws_get.py ${D}${install_dir}
  install -m 0755 localdash.py ${D}${install_dir}
  install -m 0755 recieve_node_data.py ${D}${install_dir}
  install -m 0755 server.py ${D}${install_dir}
  install -m 0644 dashboard.json ${D}${install_dir}
}

FILES_${PN} = " \
  ${install_dir}/aws_get.py \
  ${install_dir}/localdash.py \
  ${install_dir}/recieve_node_data.py \
  ${install_dir}/server.py \
  ${install_dir}/dashboard.json \
"