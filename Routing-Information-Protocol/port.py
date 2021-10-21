class port_link():
    def __init__(self, dest_IP_address, dest_port_IP, cost):
        self.dest_IP_address = dest_IP_address
        self.dest_port_IP = dest_port_IP
        self.cost = cost

    def set_dest_IP_address(self, ipAddress):
        self.dest_IP_address = ipAddress

    def set_dest_port_IP(self, portIP):
        self.dest_port_IP = portIP

    def print_link(self):
        print("destination router IP = " + str(self.dest_IP_address))
        print("destination router port IP = " + str(self.dest_port_IP))
        print("cost = " + str(self.cost))

    def return_link(self):
        p = []
        p.append("destination router IP = " + str(self.dest_IP_address))
        p.append("destination router port IP = " + str(self.dest_port_IP))
        p.append("cost = " + str(self.cost))
        return p


class port():
    def __init__(self, port_IP, link=None):
        self.port_IP = port_IP
        self.link = link

    def set_link(self, dest_router_IP_address, dest_port, cost):
        if(self.link == None):
            self.link = port_link(cost, dest_router_IP_address, dest_port)
        else:
            self.link.set_dest_port_IP = dest_port
            self.link.set_dest_IP_address = dest_router_IP_address
            self.link.cost = cost

    def get_link(self):
        return(self.link)

    def delete_link(self):
        self.link = None

    def print_port(self):
        print(str(self.port_IP) + " | " + str(self.link.dest_IP_address) +
              " | " + str(self.link.dest_port_IP) + " | " + str(self.link.cost))

    def return_port(self):
        return(str(self.port_IP) + " | " + str(self.link.dest_IP_address) + " | " + str(self.link.dest_port_IP) + " | " + str(self.link.cost))
