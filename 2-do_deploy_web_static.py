#!/usr/bin/python3
""" distributes an archive to your web servers, using the function """

from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['35.196.76.187', '34.73.234.24']
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Deploy the file in specific folders in the servers """
    if path.isfile(archive_path) is False:
        return False
    # With .tgz
    filetgz = archive_path.split("/")[-1]
    # No .tgz
    filename = filetgz.replace('.tgz', '')

    newdir = "/data/web_static/releases/" + filename

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir {}/".format(newdir))
        run("sudo tar -xzf /tmp/{} -C {}/".format(filetgz, newdir))
        run("sudo rm /tmp/{}".format(filetgz))
        run("sudo mv {}/web_static/* {}/".format(newdir, newdir))
        run("sudo rm -rf {}/web_static".format(newdir))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newdir))
        print("New version deployed!")
        return True
    except:
        return False
