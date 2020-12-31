import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_file(host):
    systemd_prefix = "/lib" if host.system_info.distribution == "ubuntu" else "/usr/lib"
    f = host.file(systemd_prefix+'/systemd/system/bitbucket.service')
    assert f.contains("^ExecStart=/opt/atlassian/bitbucket/current/bin/start-bitbucket.sh -fg --no-search >/opt/atlassian/bitbucket/current/logs/catalina.out 2>/opt/atlassian/bitbucket/current/logs/catalina.err$")
    assert f.contains("^UMask=0027$")
    assert f.contains("^LimitNOFILE=4096$")
    assert f.contains("^Environment=BITBUCKET_HOME=/media/atl/bitbucket$")
    assert f.contains("^Environment=JVM_MINIMUM_MEMORY=dummy_heap$")
    assert f.contains("^Environment=JVM_MAXIMUM_MEMORY=dummy_heap$")
    assert f.contains("^Environment=JVM_SUPPORT_RECOMMENDED_ARGS=dummy_opts$")
