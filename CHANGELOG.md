## v1.0.1 (Unreleased)

NEW FEATURES:
- Allow to configure a cronjob to cleanup old Metronome data ([\#5](https://github.com/PowerDNS/metronome-ansible/pull/5))

## v1.0.0 (2019-02-21)

__BREAKING CHANGES__:
- Do not configure the `metronome-master` repository by default ([\#4](https://github.com/PowerDNS/metronome-ansible/pull/4))

NEW FEATURES:
- Add an option to install Metronome's debug symbols package ([\#4](https://github.com/PowerDNS/metronome-ansible/pull/4))

IMPROVEMENTS:
- CI with molecule 2.14.0 ([\#5](https://github.com/PowerDNS/metronome-ansible/pull/5))

BUG FIXES:
- Do not install `yum-plugin-priorities` on RHEL ([\#4](https://github.com/PowerDNS/metronome-ansible/pull/4))

## v0.2.0 (2017-12-06)

IMPROVEMENTS:
- Switch to the MIT License ([\#2](https://github.com/PowerDNS/dnsdist-ansible/pull/2))

BUG FIXES:
- Fix the `metronome-master` YUM and APT repositories URL

## v0.1.1 (2017-05-16)

BUG FIXES:
- Fix systemd overrides template and file location

## v0.1.0 (2017-03-29)

Initial release.

NEW FEATURES:
- Metronome installation and configuration with Red-Hat and Debian support
