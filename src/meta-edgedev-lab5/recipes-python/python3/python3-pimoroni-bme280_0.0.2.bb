SUMMARY = "Python library for the bme280 temperature, pressure and humidity sensor"
HOMEPAGE = "http://www.pimoroni.com/"
AUTHOR = "Philip Howard <phil@pimoroni.com>"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE.txt;md5=990500e2985e027f34bcefb602873d7f"

SRC_URI = "https://files.pythonhosted.org/packages/11/28/89c910ba6c790f8196f47206f45f56e1437efa890ebfade6ae806ef6afa4/pimoroni-bme280-0.0.2.tar.gz"
SRC_URI[md5sum] = "0959877b4d8020a723d23ecd397d6514"
SRC_URI[sha256sum] = "25bdb567af227521b628d26df229491c45e827d1119ec693ca01ea2efd417728"

S = "${WORKDIR}/pimoroni-bme280-0.0.2"

RDEPENDS_${PN} = "python3-i2cdevice"

inherit setuptools3
