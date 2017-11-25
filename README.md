# Reverse DNS of an IP List

This is made to take an IP list and perform a reverse DNS on every IP in the list. Included is a script for sorting out the successfully reversed IPs.

It accepts IPs in the form of just the IP, or an IP:port combination. The port will be maintained throughout. The input file must have the IPs separated by lines.

First, ips.txt must be populated, then reverse-dns-ip-list.py is run, and last, filter_hosts.py is used to filter the hosts. Note that duplicate hosts on the same network will be omitted.

