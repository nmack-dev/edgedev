
SUMMARY = "FTDI device driver (pure Python)"
HOMEPAGE = "http://github.com/eblot/pyftdi"
AUTHOR = "Emmanuel Blot <emmanuel.blot@free.fr>"
LICENSE = "BSD"
LIC_FILES_CHKSUM = "file://setup.py;md5=625e1d7183ff4d5b495afdb4c84a5572"

SRC_URI = "https://files.pythonhosted.org/packages/e9/9f/6cecb794fd5a4f9f4026815e3138960aa8814634f2fa642a4c2eba980b46/pyftdi-0.42.2.tar.gz"
SRC_URI[md5sum] = "44638c3f32d52ed3b181845bd6d96031"
SRC_URI[sha256sum] = "72436911f1f5da15869027401ef666e9b0c8f051e4ba8cd32377b0757016ebae"

S = "${WORKDIR}/pyftdi-0.42.2"

RDEPENDS_${PN} = " \
  python3-pyusb \
  libusb1 \
"

inherit setuptools3
