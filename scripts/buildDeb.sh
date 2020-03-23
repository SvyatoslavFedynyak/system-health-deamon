#!/bin/bash
set -x

CUR_DIR=$(pwd)
if [[ $CUR_DIR != 'system-health-daemon' ]];then
    echo "This script should be run from project's root directory"
    exit 1
fi

make build

VERSION=1.0

mkdir deb/pkg
TEMPLATE_DIR=deb/system_health_daemon_template
DEB_DIR=deb/pkg/system_health_daemon-$VERSION
rm -rf $DEB_DIR

cp -r $TEMPLATE_DIR $DEB_DIR

cp dist/system_health_daemon-*.tar.gz $DEB_DIR/tmp/
rm -rf $DEB_DIR/tmp/package
cp system_health_daemon/config/daemon.cfg $DEB_DIR/etc/system-health-daemon/
cp system_health_daemon/config/system-health-daemon.service $DEB_DIR/lib/systemd/system/

dpkg-deb --build $DEB_DIR

rm -rf $DEB_DIR