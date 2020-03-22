#!/bin/bash

make build

TEMPLATE_DIR=deb/system_healt_daemon_template

cp dist system_health_daemon-*.tar.gz $TEMPLATE_DIR/tmp/
cp system_healt_daemon/config/daemon.cfg $TEMPLATE_DIR/etc/system-heath-daemon/
cp system_healt_daemon/config/system-health-daemon.service $TEMPLATE_DIR/lib/systemd/system/