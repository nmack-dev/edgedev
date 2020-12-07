SUMMARY = "Lab 6 Mini Project"
SECTION = "examples"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = " \
  file://proj6.py \
  file://webserver.py \
  file://index.html \
  file://placeholder.txt \
"

S = "${WORKDIR}"

install_dir = "/home/root/proj6"

do_install() {
  install -d ${D}${install_dir}
  install -m 0755 proj6.py ${D}${install_dir}
  install -m 0755 webserver.py ${D}${install_dir}
  install -m 0644 index.html ${D}${install_dir}
  install -m 0644 placeholder.txt ${D}${install_dir}
}

FILES_${PN} = " \
  ${install_dir}/proj6.py \
  ${install_dir}/webserver.py \
  ${install_dir}/index.html \
  ${install_dir}/placeholder.txt \
"