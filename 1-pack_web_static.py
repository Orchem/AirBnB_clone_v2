#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from
the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local, lcd
from datetime import datetime
from os.path import isdir


def do_pack():
    """funtion that make a webstatic pack in a .tgz
    """
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir -p versions")
        path_name = "versions/web_static_{}.tgz".format(time)
        print("Packing web_static to {}".format(path_name))
        local("tar -cvzf {} web_static/".format(path_name))
        return path_name
    except:
        return None
