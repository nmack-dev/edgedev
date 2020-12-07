FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

SRC_URI_append = " \
   file://0000-populate-resolvconf-for-nfsroot.patch \
"
