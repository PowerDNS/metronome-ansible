Metronome Ansible Role
======================

An Ansible role to install and configure [Metronome](https://github.com/ahupowerdns/metronome).

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

```
metronome_configure_repo: False
metronome_apt_repo: ""     # Metronome APT repository URL
metronome_gpg_key_url: ""  # Metronome GPG key URL
metronome_gpg_key_id: ""   # Metronome GPG key ID
metronome_yum_repo: ""     # Metronome YUM repository URL
```

If `metronome_configure_repo` is True, the role will add the metronome repository to the system.
The `metronome_apt_repo` and `metronome_yum_repo` variables should contain the URL of the repository according to the target operating system.
The specification of the GPG key through the `metronome_gpg_key_url` and `metronome_gpg_key_id` variables, althought recommended, is not mandatory.

```
metronome_user: "metronome"
metronome_group: "metronome"
```

The user and group running the metronome service.

```
metronome_carbon_address: "[::]:2003"
```

The listen address for the incoming carbon messages.

```
metronome_webserver_address: "[::]:8000"
```

The listen address for the embedded web-server.

```
metronome_stats_directory: '/var/lib/metronome'
```

The directory in which metronome will store the collected stats files.

```
metronome_replace_local_js: True
metronome_local_js_scheme: 'http'
metronome_local_js_address: "{{ ansible_default_ipv4['address'] }}"
metronome_local_js_url: '/'
```

If `metronome_replace_local_js` is set to True, the role will override the default metronome `local.js` in order to make
the metronome UI connect to the metronome instance available at `metronome_local_js_address` via `metronome_local_js_scheme`.

License
-------

(C) 2017 - PowerDNS.COM BV

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
