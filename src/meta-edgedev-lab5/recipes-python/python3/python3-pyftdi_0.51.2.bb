
SUMMARY = "FTDI device driver (pure Python)"
HOMEPAGE = "http://github.com/eblot/pyftdi"
AUTHOR = "Emmanuel Blot <emmanuel.blot@free.fr>"
LICENSE = "BSD"
LIC_FILES_CHKSUM = "file://setup.py;md5=158469856c902ab5a9a0123c0a10bdb0"

SRC_URI = "https://files.pythonhosted.org/packages/64/14/f502462dfd8045884a03eb3920d49f359cdaf38d97d367469bf84c0847ad/pyftdi-0.51.2.tar.gz"
SRC_URI[md5sum] = "d9e8d0bba091331eda6d4ea32ae0e9e2"
SRC_URI[sha256sum] = "02926258d5dfd28452a3d4d7c2f6d5bab722133b2885bde8b9e28bd2ccc095ca"

S = "${WORKDIR}/pyftdi-0.51.2"

RDEPENDS_${PN} = " \
  python3-pyusb \
  libusb1 \
"

inherit setuptools3
