SUMMARY = "Mini Progject for Lab 4 v2"
SECTION = "examples"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = " \
  file://main.py \
  file://serve-page.js \
  file://index.html \
"

S = "${WORKDIR}"

install_dir = "/home/root/lab4-project-v2"

do_install() {
  install -d ${D}${install_dir}
  install -m 0755 main.py ${D}${install_dir}
  install -m 0644 serve-page.js ${D}${install_dir}
  install -m 0644 index.html ${D}${install_dir}
}

FILES_${PN} = " \
  ${install_dir}/main.py \
  ${install_dir}/serve-page.js \
  ${install_dir}/index.html \
"