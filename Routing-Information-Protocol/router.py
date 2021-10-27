from rip_packet import RIP_entry
from rip_packet import RIP_packet
from port import port
from port import port_link


class router_base:
    def __init__(self, IP_address, rip_entries, ports):
        self.IP_address = IP_address
        self.rip_entries = rip_entries
        self.ports = ports

    def add_port(self, prt):
        self.ports.append(prt)

    def add_RIP_entry(self, port_IP, dest_IP, cost, next_hop_IP):
        new_rip_entry = RIP_entry(port_IP, cost, dest_IP, next_hop_IP)
        self.rip_entries.append(new_rip_entry)

    def find_RIP_entry(self, destination_IP_to_find):
        for entry in self.rip_entries:
            if(entry.dest_IP_address == destination_IP_to_find):
                return entry
        return None

    def set_RIP_entry_cost(self, destination_IP_to_find, new_cost):
        for i in self.rip_entries:
            if(entry.dest_IP_address == destination_IP_to_find):
                entry.set_cost(new_cost)
        return None

    def delete_RIP_entry(self, destination_IP_to_find):
        for entry in self.rip_entries:
            if(entry.dest_IP_address == destination_IP_to_find):
                self.rip_entries.remove(entry)

    def print_router(self):
        print("~~~~ Router IP address = " + str(self.IP_address) + "~~~~")
        print("---Ports---")
        print("Port IP | Destination Router IP | Destination Port IP | Cost")
        for p in self.ports:
            p.print_port()
        print("---RIP entries---")
        print("port IP | destination IP address | next hop | cost")
        for re in self.rip_entries:
            re.print_rip_entry()

    def return_router(self):
        r = []
        r.append("~~~~ Router IP address = " + str(self.IP_address) + "~~~~")
        r.append("---Ports---")
        r.append("Port IP | Destination Router IP | Destination Port IP | Cost")
        for p in self.ports:
            r.append(p.return_port())
        r.append("---RIP entries---")
        r.append("port IP | destination IP address | next hop | cost")
        for re in self.rip_entries:
            r.append(re.return_rip_entry())
        return r


class router(router_base):
    def send_RIP_packets(self, routers):
        self.rip_packet = RIP_packet(self.rip_entries)
        for i in range(len(routers)):  # Find all neighbors and send then RIP packet
            for j in range(len(self.ports)):
                if routers[i].IP_address == self.ports[j].link.dest_IP_address:
                    routers = routers[i].receive_RIP_packets(
                        self.rip_packet, self.ports[j].link, routers, self.IP_address)
        return routers

    def receive_RIP_packets(self, rip_packet, link_send_on, routers, next_hop_IP):
        found = 0
        new_rip_entries = []
        for i in range(len(rip_packet.rip_entries)):
            for j in range(len(self.rip_entries)):
                # If entry exists
                if(rip_packet.rip_entries[i].dest_IP_address == self.rip_entries[j].dest_IP_address):
                    found = 1
                    new_cost = link_send_on.cost + \
                        rip_packet.rip_entries[i].cost
                    # If next hop is listed as the router received from
                    if(self.rip_entries[j].next_hop_IP == next_hop_IP and self.rip_entries[j].cost != new_cost):
                        self.rip_entries[j].cost = min(16, new_cost)
                        break
                    elif(new_cost < self.rip_entries[j].cost):
                        self.rip_entries[j].cost = new_cost
                        self.rip_entries[j].next_hop_IP = next_hop_IP
                        break
            # If entry does not already exist
            if(not found):
                new_rip_entries.append(RIP_entry(
                    link_send_on.dest_port_IP, rip_packet.rip_entries[i].cost+link_send_on.cost, rip_packet.rip_entries[i].dest_IP_address, next_hop_IP))
            found = 0
        self.rip_entries.extend(new_rip_entries)
        return routers
