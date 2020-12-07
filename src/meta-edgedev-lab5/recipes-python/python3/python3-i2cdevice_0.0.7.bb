SUMMARY = "Python DSL for interacting with SMBus-compatible i2c devices"
HOMEPAGE = "http://www.pimoroni.com/"
AUTHOR = "Philip Howard <phil@pimoroni.com>"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE.txt;md5=f1e0f2765d0deb24be669d1789b957d7"

SRC_URI = "https://files.pythonhosted.org/packages/89/61/8b234494fa4f8f551ab82c319417a2bb44cc32573764fe97dc3b2acb050c/i2cdevice-0.0.7.tar.gz"
SRC_URI[md5sum] = "c69568277a0ff858a1b1a70cfba4ddc7"
SRC_URI[sha256sum] = "fb6dafcbf654a9de732adb51c99a0aded31cfa924ea0b78b1583944c00a9235c"

S = "${WORKDIR}/i2cdevice-0.0.7"

inherit setuptools3

