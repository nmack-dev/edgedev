SUMMARY = "Pure-python FIGlet implementation"
HOMEPAGE = "https://github.com/pwaller/pyfiglet"
AUTHOR = "Christopher Jones <cjones@insub.org>"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=f37a72c457e560fc4853ae67f3f9cc0e"

SRC_URI = "https://files.pythonhosted.org/packages/f9/02/48293654fb2e4fdeb4d927f00a380230a832744b6c9af757373a72d018d1/pyfiglet-0.8.post1.tar.gz"
SRC_URI[md5sum] = "2e1d6f0668e9cb1ffacee307ca4b778a"
SRC_URI[sha256sum] = "c6c2321755d09267b438ec7b936825a4910fec696292139e664ca8670e103639"

S = "${WORKDIR}/pyfiglet-0.8.post1"

inherit setuptools3
