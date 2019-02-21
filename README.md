# Ansible Role: Metronome

An Ansible role to install and configure [Metronome](https://github.com/ahupowerdns/metronome).

[![Build Status](https://travis-ci.org/PowerDNS/metronome-ansible.svg?branch=master)](https://travis-ci.org/PowerDNS/metronome-ansible)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-PowerDNS.metronome-blue.svg)](https://galaxy.ansible.com/PowerDNS/metronome)
[![GitHub tag](https://img.shields.io/github/tag/PowerDNS/metronome-ansible.svg)](https://github.com/PowerDNS/metronome-ansible/tags)

## Requirements

An Ansible 2.2 or higher installation.

## Dependencies

None.

## Role Variables

Available variables are listed below, along with default values (see defaults/main.yml):

    metronome_install_repo: ""

By default, Metronome is installed from the repositories available on the host.

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

    metronome_service_overrides: {}

Dict with overrides for the service (systemd only).
This can be used to change any systemd settings in the `[Service]` category

## Changelog

A detailed changelog of all the changes applied to the role is available [here](./CHANGELOG.md).

## Testing

Tests are performed by [Molecule](http://molecule.readthedocs.org/en/latest/).

    $ pip install tox

To test all the scenarios run

    $ tox

To run a custom molecule command

    $ tox -e py27-ansible22 -- molecule test -s metronome-master

## License

MIT
