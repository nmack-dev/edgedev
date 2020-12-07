SUMMARY = "Lab 7 Mini Project"
SECTION = "examples"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = " \
  file://webserver.py \
  file://note_recognition.py \
  file://utils.py \
"

S = "${WORKDIR}"

install_dir = "/home/root/proj7"

do_install() {
  install -d ${D}${install_dir}
  install -m 0755 note_recognition.py ${D}${install_dir}
  install -m 0755 webserver.py ${D}${install_dir}
  install -m 0755 utils.py ${D}${install_dir}
}

FILES_${PN} = " \
  ${install_dir}/note_recognition.py \
  ${install_dir}/webserver.py \
  ${install_dir}/utils.py \
"