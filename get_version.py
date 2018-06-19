'''
Source 
https://github.com/smarie/env-switcher-gui/blob/master/envswitch/utils.py
'''
def get_version():
    """
    Utility to find the version of this application whatever the execution mode (cx_Freeze or normal)
    :return:
    """
    if getattr(sys, "frozen", False):
        # this is cx_Freeze execution mode >> access our generated file
        datadir = os.path.dirname(sys.executable)
        path = os.path.join(datadir, version_file_cx_freeze)
        with open(path, 'rt') as f:
            return f.read()
    else:
        import pkg_resources  # part of setuptools
        from pkg_resources import DistributionNotFound
        try:
            return pkg_resources.require("envswitch")[0].version
        except DistributionNotFound as e:
            # this may happen if the module has not been even locally installed with "pip install ."
            from setuptools_scm import get_version
            return get_version() 
