#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers,
 using the function do_deploy
"""

from fabric.api import env, run, put
from datetime import datetime
from os.path import isdir, exists
env.hosts = ['3.238.254.219', '3.236.232.84']


def do_deploy(archive_path):
    """deploy a webservers
    """
    if exists(archive_path):
        try:
            filename = archive_path.split("/")[-1]
            not_ext = filename.split(".")[0]
            not_path = "/data/web_static/releases/{}/".format(not_ext)
            put(archive_path, "/tmp/")
            run("mkdir -p {}{}".format(not_path, not_ext))
            run("tar -xzf /tmp/{} -C {}{}".format(filename, not_path, not_ext))
            run("rm /tmp/{}".format(filename))
            run("mv {0}{1}/web_static/* {0}{1}/".format(not_path, not_ext))
            run("rm -rf {}{}web_static".format(not_path, not_ext))
            run("rm -rf /data/web_static/current")
            run("ln -s {}{}/ /data/web_static/current".format(
                not_path, not_ext))
            return True
        except:
            print("f")
            return False
    else:
        print("x")
        return False
