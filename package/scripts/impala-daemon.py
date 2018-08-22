# -*- coding: utf-8 -*-
from resource_management import *
from impala_base import ImpalaBase


class ImpalaDaemon(ImpalaBase):
    # Call setup.sh to install the service
    def install(self, env):

        # Install packages listed in metainfo.xml
        self.install_packages(env)
        self.installImpala(env)
        self.configure(env)
        self.configureHDFS(env)

    def configure(self, env):
        self.configureImpala(env)

    # Call start.sh to start the service
    def start(self, env):
        # self.configure(env)
        cmd = 'service impala-server start'
        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)

    # Called to stop the service using the pidfile
    def stop(self, env):
        cmd = 'service impala-server stop'
        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)

    # Called to get status of the service using the pidfile
    def status(self, env):
        check_process_status("/var/run/impala/impalad-impala.pid")


if __name__ == "__main__":
    ImpalaDaemon().execute()
