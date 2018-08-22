# -*- coding: utf-8 -*-
from resource_management import *
from impala_base import ImpalaBase


class StateStore(ImpalaBase):
    # Call setup.sh to install the service
    def install(self, env):

        # Install packages listed in metainfo.xml
        self.install_packages(env)
        self.installImpala(env)
        Execute("yum -y install python-devel openssl-devel python-pip cyrus-sasl cyrus-sasl-gssapi cyrus-sasl-devel")
        self.configure(env)

    def configure(self, env):
        self.configureImpala(env)

    # Call start.sh to start the service
    def start(self, env):
        # self.configure(env)
        cmd = 'service impala-state-store start'
        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)

    # Called to stop the service using the pidfile
    def stop(self, env):
        cmd = 'service impala-state-store stop'
        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)

    # Called to get status of the service using the pidfile
    def status(self, env):
        check_process_status("/var/run/impala/statestored-impala.pid")


if __name__ == "__main__":
    StateStore().execute()
