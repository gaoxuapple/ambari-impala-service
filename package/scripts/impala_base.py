# -*- coding: utf-8 -*-
from resource_management import *
import os


class ImpalaBase(Script):
    impala_packages = [
        'impala-server',
        'impala-catalog',
        'impala-state-store',
        'impala-shell']
    # Call setup.sh to install the service

    def installImpala(self, env):
        # Install packages listed in metainfo.xml
        self.install_packages(env)
        if self.impala_packages is not None and len(self.impala_packages):
            for pack in self.impala_packages:
                Package(pack)
        import params
        env.set_params(params)

        scriptDir = params.files_dir
        datalakeJar = None
        for dir in os.listdir(scriptDir):
            if dir.startswith('hadoop-azure-datalake') and dir.endswith(".jar"):
                datalakeJar = dir
        if datalakeJar is None:
            raise Exception("Couldn't find hadoop-azure-datalake-*.jar in " + scriptDir)
        File(
            "/usr/lib/impala/lib/"+datalakeJar,
            content=StaticFile(os.path.join(scriptDir,datalakeJar)), mode=0o644)
        # init lib
        File(format("{tmp_dir}/impala_init_lib.sh"),
             content=Template('init_lib.sh.j2',datalakeJar=datalakeJar), mode=0o700)
        Execute(format("bash {tmp_dir}/impala_init_lib.sh"))

    def configureImpala(self, env):
        import params
        env.set_params(params)
        # if params.security_enabled:
        #     cmd = format("{service_packagedir}/scripts/ktuntil_config.sh")
        #     Execute('echo "Running ' + cmd + '" as root')
        #     Execute(cmd, ignore_failures=True)
        realm_name = os.popen(
            'grep "default_realm" /etc/krb5.conf ').read().strip(os.linesep).split(' ')[-1]
        File("/etc/default/impala",
             content=Template("impala.j2", realm_name=realm_name),
             mode=0o644
             )
        Directory(format('{impala_scratch_dir}'), mode=0o777)
        self.configureHDFS(env)

    def configureHDFS(self, env):
        import params
        for service_name in params.scp_conf_from.keys():
            if params.scp_conf_from[service_name]["host"]:
                for fndir in params.scp_conf_from[service_name]["files"]:
                    fn = os.path.split(fndir)[-1]
                    Execute(
                        format(
                            "scp -r root@%s:%s {tmp_dir}" %
                            (params.scp_conf_from[service_name]["host"], fndir)))
                    File(format("{scp_conf_dir}/%s" % fn),
                         content=StaticFile(format("{tmp_dir}/%s" % fn)),
                         mode=0o644,
                         encoding="utf-8")
