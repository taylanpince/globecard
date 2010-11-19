from fabric.api import *
from fabric.contrib.console import confirm


env.root_dir = "/home/globecardteam/sites/globecard"
env.project_dir = "%s/src/globecard" % env.root_dir
env.user = "globecardteam"
env.hosts = [
    "38.112.106.94:8022",
]

def deploy():
    """
    Deploy the latest version
    """
    update()
    update_pip()
    syncdb()
    restart()

def update():
    """
    Updates project source
    """
    run('cd %s; git pull' % env.project_dir)

def version():
    """
    Show last commit to repo on server
    """
    run('cd %s; git log -1' % env.project_dir)

def restart():
    """
    Restart Apache process
    """
    run('touch %s/conf/globecard.wsgi' % env.project_dir)

def update_pip():
    """
    Update pip requirements
    """
    virtualenv_run('pip install -E %s -r %s/conf/requirements.pip' % (env.root_dir, env.project_dir))

def syncdb():
    """
    Run syncdb and apply south migrations
    """
    virtualenv_run('manage.py syncdb')
    virtualenv_run('manage.py migrate')

def virtualenv_run(cmd):
    """
    Runs a command using the virtualenv environment
    """
    require('root_dir')

    return run('source %s/bin/activate; %s' % (env.root_dir, cmd))
