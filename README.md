Metronome Ansible Role
======================

An Ansible role to install and configure [Metronome](https://github.com/ahupowerdns/metronome).

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

    metronome_install_repo: "{{ metronome_powerdns_repo_master }}"

By default Metronome is installed from the repositories available on the host.

    metronome_install_repo: "{{ metronome_powerdns_repo_master }}"

Master build of Metronome can be installed setting the `metronome_install_repo` variable as shown above.

    metronome_install_debug_symbols_package: False

Install Metronome symbols package

    metronome_user: "metronome"
    metronome_group: "metronome"

The user and group running the metronome service.

    metronome_carbon_address: "[::]:2003"

The listen address for the incoming carbon messages.

    metronome_webserver_address: "[::]:8000"

The listen address for the embedded web-server.

    metronome_stats_directory: '/var/lib/metronome'

The directory in which metronome will store the collected stats files.

    metronome_replace_local_js: True
    metronome_local_js_scheme: 'http'
    metronome_local_js_address: "{{ ansible_default_ipv4['address'] }}"
    metronome_local_js_url: '/'

If `metronome_replace_local_js` is set to True, the role will override the default metronome `local.js` in order to make
the metronome UI connect to the metronome instance available at `metronome_local_js_address` via `metronome_local_js_scheme`.

License
-------

MIT
