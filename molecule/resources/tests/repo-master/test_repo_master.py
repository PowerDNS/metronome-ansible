
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']


def test_metronome_repo(host):
    f = None
    if host.system_info.distribution.lower() in debian_os:
        f = host.file('/etc/apt/sources.list.d/metronome-master.list')
    if host.system_info.distribution.lower() in rhel_os:
        f = host.file('/etc/yum.repos.d/metronome-master.repo')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('metronome-master')
