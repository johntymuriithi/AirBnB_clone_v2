#!/usr/bin/python3

""" Fabric Module to generate .tgz archive from contents of specific folder.
"""

from fabric import task
from fabric.operations import local
from datetime import datetime

@task
def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Generate the name for the archive
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(now)

    # Create the archive
    result = local("tar -cvzf versions/{} web_static".format(archive_name), capture=True)

    if result.failed:
        return None
    else:
        return "versions/{}".format(archive_name)