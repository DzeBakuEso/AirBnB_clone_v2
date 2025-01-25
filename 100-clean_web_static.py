#!/usr/bin/python3
from fabric.api import *
import os

env.hosts = ['<IP web-01>', '<IP web-02>']

def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep. Defaults to 0.
    """
    number = 1 if int(number) == 0 else int(number)

    # Local cleanup of archives in the versions folder
    local_archives = sorted(os.listdir("versions"))
    archives_to_delete = local_archives[:-number]

    with lcd("versions"):
        for archive in archives_to_delete:
            local("rm -f {}".format(archive))

    # Remote cleanup of archives in the releases folder on both servers
    releases_dir = "/data/web_static/releases"
    with cd(releases_dir):
        remote_archives = run("ls -tr").split()
        remote_archives = [a for a in remote_archives if "web_static_" in a]
        archives_to_delete = remote_archives[:-number]

        for archive in archives_to_delete:
            run("rm -rf {}".format(archive))
