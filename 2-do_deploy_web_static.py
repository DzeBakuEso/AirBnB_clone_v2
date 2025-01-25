#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers.
"""
from fabric.api import env, put, run
import os

# Define the web server hosts
env.hosts = ['xx-web-01', 'xx-web-02']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    Args:
        archive_path (str): The path to the archive.
    Returns:
        True if all operations are successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract the archive name and folder name
        archive_file = archive_path.split("/")[-1]
        archive_name = archive_file.split(".")[0]
        release_folder = "/data/web_static/releases/{}".format(archive_name)

        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, "/tmp/{}".format(archive_file))

        # Create the release folder
        run("mkdir -p {}".format(release_folder))

        # Uncompress the archive into the release folder
        run("tar -xzf /tmp/{} -C {}".format(archive_file, release_folder))

        # Remove the archive from the web server
        run("rm /tmp/{}".format(archive_file))

        # Move the contents out of the web_static folder
        run("mv {}/web_static/* {}".format(release_folder, release_folder))

        # Remove the now-empty web_static folder
        run("rm -rf {}/web_static".format(release_folder))

        # Delete the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link to the release folder
        run("ln -s {} /data/web_static/current".format(release_folder))

        print("New version deployed!")
        return True

    except Exception as e:
        print("An error occurred: {}".format(e))
        return False
