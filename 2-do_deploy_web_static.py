#!/usr/bin/python3
"""Module to make .tgz file from local directory"""


import datetime
import fabric.api
import os

fabric.api.env.hosts = ['35.229.22.85', '34.74.166.73']


def do_pack():
    """Compress local web static files"""

    if not os.path.isdir("versions"):
        os.mkdir("versions")
    target = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    target = "versions/web_static_" + target + ".tgz"
    fabric.api.local("tar -cvzf " + target + " web_static")
    return target

def do_deploy(path):
    """Distributes .tgz file to servers"""

    date = path[-18:-4]
    if not os.path.isfile(path):
        return False
    fabric.api.put("versions/web_static_{}.tgz".format(date), "/tmp/")
    fabric.api.run("mkdir -p /data/web_static/"
                   "releases/web_static_{}/".format(date))
    fabric.api.run("tar -xzf /tmp/web_static_{}.tgz -C /data/web_static/"
                   "releases/web_static_{}".format(date, date))
    fabric.api.run("rm /tmp/web_static_{}.tgz".format(date))
    fabric.api.run("mv /data/web_static/releases/web_static_{}/"
                   "web_static/* /data/web_status/releases/"
                   "web_static_{}/".format(date, date))
    fabric.api.run("rm -rf /data/web_static/releases/"
                   "web_static_{}/web_static".format(date))
    res = fabric.api.run("rm -rf /data/web_static/current")
    fabric.api.run("ln -s /data/web_static/releases/web_"
                   "static_{}/ /data/web_static/current".format(date))
    return True
