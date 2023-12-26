# -*- coding:utf-8 -*-

from pkg_resources import resource_filename

def grp(relative_path : str) -> str:
    ''' Get resource path of the package '''
    grp_path = resource_filename(__name__, relative_path)
    return_path = grp_path.replace('\\common','').replace('\\app\\app','\\app').replace('\\app\\common','')
    return return_path