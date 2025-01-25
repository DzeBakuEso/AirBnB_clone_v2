#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder in the AirBnB Clone repo.
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns:
        The archive path if successful, otherwise None.
    """
    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Format the archive name with the current timestamp
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)

    # Create the archive
    try:
        print("Packing web_static to {}".format(archive_name))
        local("tar -cvzf {} web_static".format(archive_name))
        archive_size = os.path.getsize(archive_name)
        print("web_static packed: {} -> {}Bytes"
              .format(archive_name, archive_size))
        return archive_name
    except Exception as e:
        print("An error occurred: {}".format(e))
        return None
