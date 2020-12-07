SUMMARY = "Reads temperature from the bme280 sensor"
SECTION = "examples"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

RDEPENDS_${PN} = " \
  python3-pyftdi \
  python3-pimoroni-bme280 \
"

SRC_URI = " \
  file://read-bme280.py \
"

S = "${WORKDIR}"

install_dir = "/home/root/${PN}"

do_install() {
  install -d ${D}${install_dir}
  install -m 0755 ${S}/read-bme280.py ${D}${install_dir}/read-bme280.py
}

FILES_${PN} = " \
  ${install_dir}/read-bme280.py \
"