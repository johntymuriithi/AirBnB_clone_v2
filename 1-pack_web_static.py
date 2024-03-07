#!/usr/bin/python3
#Fabric Module to generate .tgz archive from contents of specific folder.

from fabric.operations import local
from datetime import datetime

def do_pack():
    #Generates a .tgz archive from the contents of the web_static folder."""
    local("mkdir -p versions")

    # Generate the name for the archive
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(now)

    result = local("tar -cvzf versions/{} web_static".format(archive_name), capture=True)

    if result.failed:
        return None
    else:
        return "versions/{}".format(archive_name)
