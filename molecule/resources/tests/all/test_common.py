import os
import yaml
import pytest
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']


@pytest.fixture()
def AnsibleVars(host):
    varsFiles = ['../../vars/main.yml']
    if host.system_info.distribution.lower() in debian_os:
        varsFiles.append('../../vars/Debian.yml')
    if host.system_info.distribution.lower() in rhel_os:
        varsFiles.append('../../vars/RedHat.yml')

    ansibleVars = {}
    for f in varsFiles:
        with open(f, 'r') as stream:
            ansibleVars.update(yaml.load(stream))

    return ansibleVars


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_package(host):
    p = host.package('metronome')
    assert p.is_installed


def test_service(host):
    # Using Ansible to mitigate some issues with the service test on debian-8
    s = host.ansible('service', 'name=metronome state=started enabled=yes')
    assert s['changed'] is False


def test_localjs_config(host, AnsibleVars):
    f = host.file('/usr/share/metronome/html/local.js')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0644'


def test_service_config(host):
    f = None
    smgr = host.ansible('setup')['ansible_facts']['ansible_service_mgr']
    if smgr == 'systemd':
        f = host.file('/etc/systemd/system/metronome.service.d/override.conf')
        assert 'LimitCORE=infinity' in f.content
    else:
        f = host.file('/etc/default/metronome')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0644'


def test_cleanup_cronjob(host):
    f = None
    if host.system_info.distribution.lower() in debian_os:
        f = host.file('/var/spool/cron/crontabs/root')
    if host.system_info.distribution.lower() in rhel_os:
        f = host.file('/var/spool/cron/root')

    assert f.exists
    assert '15 2 * * * find /var/lib/metronome/ -mtime +5 -delete' in f.content
