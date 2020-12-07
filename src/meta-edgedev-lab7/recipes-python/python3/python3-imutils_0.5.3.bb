SUMMARY = "A series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, displaying Matplotlib images, sorting contours, detecting edges, and much more easier with OpenCV and both Python 2.7 and Python 3."
HOMEPAGE = "https://github.com/jrosebr1/imutils"
AUTHOR = "Adrian Rosebrock <adrian@pyimagesearch.com>"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://setup.py;md5=64e977f8136550e805494226326f6fa8"

SRC_URI = "https://files.pythonhosted.org/packages/b5/94/46dcae8c061e28be31bcaa55c560cb30ee9403c9a4bb2659768ec1b9eb7d/imutils-0.5.3.tar.gz"
SRC_URI[md5sum] = "8c2a1cbf774f35fbb9dffd26df0c4bff"
SRC_URI[sha256sum] = "857af6169d90e4a0a814130b9b107f5d611150ce440107e1c1233521c6fb1e2b"

S = "${WORKDIR}/imutils-0.5.3"

RDEPENDS_${PN} = ""

inherit setuptools3
