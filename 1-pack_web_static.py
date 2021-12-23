#!/usr/bin/python3
from datetime import datetime
from fabric.api import *
'''fabric script to fgenerate tgz archive
'''


def do_pack():
    '''making a pack on web_static folder
    '''
    now = datetime.now()
    file = 'web_static_' + now.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local("mkdir -p versions")
    check = local("tar -cvzf versions/{file} web_static".format(file=file))
    if check is not None:
        return file
    else:
        return None
