DESCRIPTION = "Wrapper package for OpenCV python bindings."
HOMEPAGE = "https://github.com/skvark/opencv-python"
AUTHOR = "Olli-Pekka Heinisuo"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE.txt;md5=c4a59ea6fdfe49caa8470881ba0a6ffa"

PYPI_PACKAGE = "opencv-python-headless"

SRC_URI[md5sum] = "33a295e617453286d29e6f9f0a1a0a37"
SRC_URI[sha256sum] = "6eefcacfb9b2da305277e1a93c7bf074dcd10b7aa154a0c963ded08fc0ffc02e"

SRC_URI += "file://opencv_python_detection.patch"

inherit pypi setuptools3

#EXTRA_OECMAKE += " \
#  -DPYTHON_DESIRED=3 \
#  -DPYTHON_DEFAULT_EXECUTABLE=$(which python3) \
#  -DBUILD_NEW_PYTHON_SUPPORT=ON \
#  -DBUILD_opencv_python3=ON \
#  -DHAVE_opencv_python3=ON \
#  -DZLIB_ROOT=\"/home/iotuser/yocto/build/tmp/work/core2-32-poky-linux/zlib-intel/1.2.11.1.jtkv6.3-r0/sysroot-destdir/\" \
#  -DZLIB_LIBRARIES=\"/home/iotuser/yocto/build/tmp/work/core2-32-poky-linux/zlib-intel/1.2.11.1.jtkv6.3-r0/sysroot-destdir/usr/lib/libz.so\" \
#"

#export CMAKE_ARGS = "-DZLIB_ROOT=/home/iotuser/yocto/build/tmp/work/core2-32-poky-linux/zlib-intel/1.2.11.1.jtkv6.3-r0/sysroot-destdir/usr"
export CMAKE_ARGS = "-DZLIB_ROOT=${WORKDIR}/../../zlib-intel/1.2.11.1.jtkv6.3-r0/sysroot-destdir/usr"
#export CMAKE_ARGS = "-DZLIB_ROOT=../../zlib-intel/1.2.11.1.jtkv6.3-r0/sysroot-destdir/usr"


#export CMAKE_ARGS = "-DZLIB_LIBRARIES=/home/iotuser/yocto/build/tmp/work/core2-32-poky-linux/zlib-intel/1.2.11.1.jtkv6.3-r0/sysroot-destdir/usr/lib/libz.so"

DEPENDS += " \
  python3-scikit-build-native \
  python3-wheel-native \
  python3-distro-native \
  python3-numpy-native \
  cmake-native \
  ninja-native \
  zlib-intel \
"

RDEPENDS_${PN} += "\
  python3-numpy \
"
