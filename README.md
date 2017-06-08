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

By default Metronome is installed from the master repository.
To install Metronome from a custom repository, override the `metronome_install_repo` default value in your playbook
as shown below

    - hosts: all
      vars:
        metronome_install_repo:
          apt_repo: "deb http://my.repo.com/{{ ansible_distribution | lower }} {{ ansible_distribution_release | lower }}/metronome main"
          gpg_key: "http://my.repo.com/MYREPOGPGPUBKEY.asc" # repository's public GPG key
          gpg_key_id: "MYREPOGPGPUBKEYID"                   # to avoid to reimport the key each time the role is executed
          yum_repo_baseurl: "http://my.repo.com/centos/$basearch/$releasever/metronome"
          yum_repo_name: "metronome"
      roles:
        - { role: PowerDNS.metronome }

If `metronome_configure_repo` is True, the role will add the metronome repository to the system.
The `metronome_apt_repo` and `metronome_yum_repo` variables should contain the URL of the repository according to the target operating system.
The specification of the GPG key through the `metronome_gpg_key_url` and `metronome_gpg_key_id` variables, although recommended, is not mandatory.

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

(C) 2017 - PowerDNS.COM BV

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
