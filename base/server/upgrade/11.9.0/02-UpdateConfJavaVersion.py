#
# Copyright Red Hat, Inc.
#
# SPDX-License-Identifier: GPL-2.0-or-later
#
import logging
import re

import pki
logger = logging.getLogger(__name__)

class UpdateConfJavaVersion(pki.server.upgrade.PKIServerUpgradeScriptlet):

    def __init__(self):
        super().__init__()
        self.message = "Update Conf Java Version"

    def upgrade_instance(self, instance):

        # Updating /etc/pki/<instance>/tomcat.conf
        logger.info(f"Updating {instance.tomcat_conf}")
        self.backup(instance.tomcat_conf)

        self.update_conf_java_version(self, instance.tomcat_conf)

    

    def update_conf_java_version(self, path):
        conf_file = []
        old_java_path = r'JAVA_HOME="/usr/lib/jvm/jre-1.8.0-openjdk"'
        new_java_path = r'JAVA_HOME="/usr/lib/jvm/jre-17-openjdk"'

        with open(path, 'r', encoding="utf-8") as f:
            conf_file = f.read()
        
        conf_file = re.sub(old_java_path, new_java_path, conf_file)

        with open(path, "w", encoding="utf-8") as f:
            f.write(conf_file)

        return 