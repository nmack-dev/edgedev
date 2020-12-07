PACKAGECONFIG_append = " gles2 eglfs linuxfb fontconfig"
PACKAGECONFIG_CONFARGS = " -nomake tests -nomake examples"
DISTRO_FEATURES_remove = " x11 wayland tests xcb"

do_install_append() {
  install -d ${D}${sysconfdir}/profile.d
  echo "export QT_QPA_PLATFORM=linuxfb" > ${D}${sysconfdir}/profile.d/qt5-env.sh
}

FILES_${PN} += "${sysconfdir}/profile.d/qt5-env.sh"
