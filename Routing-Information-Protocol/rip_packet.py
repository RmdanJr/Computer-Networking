class RIP_entry:
    def __init__(self, port_IP, cost, dest_IP_address, next_hop_IP):
        self.port_IP = port_IP
        self.cost = cost
        self.dest_IP_address = dest_IP_address
        self.next_hop_IP = next_hop_IP

    def get_port_IP(self):
        return(self.port_IP)

    def set_port_IP(self, port_ip):
        self.port_IP = port_ip

    def get_cost(self):
        return self.cost

    def set_cost(self, Cost):
        self.cost = Cost

    def get_dest_dddress(self):
        return self.dest_IP_address

    def set_dest_dddress(self, destIPaddress):
        self.dest_IP_address = destIPaddress

    def get_next_hop(self):
        return(self.next_hop_IP)

    def set_next_hop(self, next_hop):
        self.next_hop_IP = next_hop

    def print_rip_entry(self):
        print(str(self.port_IP) + " | " + str(self.dest_IP_address) +
              " | " + str(self.next_hop_IP) + " | " + str(self.cost))


class RIP_packet:
    def __init__(self, rip_entries):
        self.rip_entries = rip_entries

    def add_rip_entry(self, rip_entry):
        self.rip_entries.append(rip_entry)

    def add_rip_entries(self, rip_entriess):
        self.rip_entries.extend(rip_entriess)

    def print_rip_packet(self):
        for i in range(self.rip_entry_count):
            print("RIP entry #: " + i + ":\n")
            self.rip_entries[i].print_rip_entry()

    def return_rip_packet(self):
        rp = []
        for i in range(self.rip_entry_count):
            rp.append("RIP entry #: " + i + ":\n")
            rp[i].return_rip_entry()
        return rp
