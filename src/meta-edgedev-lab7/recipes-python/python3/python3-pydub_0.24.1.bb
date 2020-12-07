DESCRIPTION = "A library that processes and analyses sound files"
HOMEPAGE = "https://github.com/jiaaro/pydub"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=d41d8cd98f00b204e9800998ecf8427e"
#S = "${WORKDIR}/git"

DEPENDS += " \
    python3 \
    python3-native \
"

RDEPENDS_${PN} = "python3"

PYPI_PACKAGE = "pydub"

SRCREV = "${AUTOREV}"
SRC_URI[sha256sum] = "630c68bfff9bb27cbc5e1f02923f717c3bc5f4d73fd685fda08b6ce90f76dc69"

SRC_URI = "git://github.com/jiaaro/pydub.git;protocol=http"

inherit pypi
inherit setuptools3
inherit native