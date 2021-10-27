from ports import ports


def is_better(BPDU1, BPDU2):
    # If root is greater than BPDU1 is better
    if(BPDU1[0] < BPDU2[0]):
        return 1
    elif(BPDU1[0] == BPDU2[0] and BPDU1[1] < BPDU2[1]):
        return 1
    elif(BPDU1[0] == BPDU2[0] and BPDU1[1] == BPDU2[1] and BPDU1[2] < BPDU2[2]):
        return 1
    elif(BPDU1[0] == BPDU2[0] and BPDU1[1] == BPDU2[1] and BPDU1[2] == BPDU2[2] and BPDU1[3] < BPDU2[3]):
        return 1
    else:
        return 0


class bridge:
    def __init__(self, bridge_ID, port_list):
        self.bridge_ID = bridge_ID
        # port_list[0] is the port with port number 0
        self.port_list = port_list
        # Root ID, Cost, Transmitting Bridge ID, Transmitting Mac Address
        self.config_BPDU = [bridge_ID, 0, bridge_ID, None]
        self.receive_queue = {}

    def initialize_recv_queue(self, bridges_dict):
        for b in bridges_dict:
            self.receive_queue[b] = []

    def set_bridge(self, bridge_ID, num_ports, mac_addresses):
        self.bridge_ID = bridge_ID
        self.num_ports = num_ports
        self.port_list = port_list

    def get_port(self, bridge_number, bridges_dict):
        for i in range(len(self.port_list)):
            if(bridge_number in self.port_list[i].get_reachable_bridge_ID(bridges_dict, self.bridge_ID)):
                return i

    def find_best_BPDUs_received(self, bridges_dict):
        # Select best BPDU at each bridge
        best_BPDUs_recvd = {}  # Bridge Number : BPDU
        best_bpdu = 0
        for sending_brg_id in self.receive_queue:
            if(len(self.receive_queue[sending_brg_id]) > 0):
                best_bpdu = self.receive_queue[sending_brg_id][0]
                for bpdu in self.receive_queue[sending_brg_id]:
                    if is_better(bpdu, best_bpdu):
                        best_bpdu = bpdu
                best_BPDUs_recvd[sending_brg_id] = best_bpdu
        self.initialize_recv_queue(bridges_dict)
        return best_BPDUs_recvd

    def update_ports(self, bridges_dict, best_BPDUs_recvd):
        for sending_brg_id in best_BPDUs_recvd:
            if sending_brg_id is not self.config_BPDU[0]:
                if self.port_list[self.get_port(sending_brg_id, bridges_dict)].port_type != 2:
                    pn = self.get_port(sending_brg_id, bridges_dict)
                    if(is_better(best_BPDUs_recvd[sending_brg_id], self.get_config_BPDU_at_port(pn))):
                        self.port_list[self.get_port(
                            sending_brg_id, bridges_dict)].port_type = 0
                    else:
                        self.port_list[self.get_port(
                            sending_brg_id, bridges_dict)].port_type = 1

    def elect_root(self, bridges_dict, best_BPDUs_recvd):
        for sending_brg_id in best_BPDUs_recvd:
            if(best_BPDUs_recvd[sending_brg_id][0] < self.config_BPDU[0]):
                # New root bridge
                self.config_BPDU[0] = best_BPDUs_recvd[sending_brg_id][0]
                self.config_BPDU[1] = best_BPDUs_recvd[sending_brg_id][1] + 1
                self.config_BPDU[2] = self.bridge_ID
                self.config_BPDU[3] = self.get_port(
                    sending_brg_id, bridges_dict)
                if(self.get_root_port_id() is not None):
                    self.port_list[self.get_root_port_id()].port_type = 1
                self.port_list[self.get_port(
                    sending_brg_id, bridges_dict)].port_type = 2

    def send_BPDUs(self, bridges_dict):
        # Find all neighbors
        for p in self.port_list:
            if(p.get_port_state() > 0):  # If sending port
                # Send to all bridges on that segment
                for b in p.get_reachable_bridge_ID(bridges_dict, self.bridge_ID):
                    pn = self.get_port(b, bridges_dict)
                    bridges_dict[b].receive_queue[self.bridge_ID].append(
                        self.get_config_BPDU_at_port(pn))
        return(bridges_dict)

    def receive_BPDUs(self, bridges_dict):
        # Update the bridge's state according to the best BPDUs received
        # Find best BPDU received from each bridge
        best_BPDUs_recvd = self.find_best_BPDUs_received(bridges_dict)

        # Compare BPDUs with those received at non-root ports
        self.update_ports(bridges_dict, best_BPDUs_recvd)

        # Find root bridge
        self.elect_root(bridges_dict, best_BPDUs_recvd)

        # Update dictionary and return
        bridges_dict[self.bridge_ID] = self
        return bridges_dict

    def get_root_port_id(self):
        for p in range(len(self.port_list)):
            if self.port_list[p].port_type == 2:
                return p
        return None

    def get_config_BPDU_at_port(self, port_number):
        BPDU_at_port = self.config_BPDU
        BPDU_at_port[3] = self.port_list[port_number].mac_address
        return(BPDU_at_port)

    def print_bridge(self):
        print("~~~~~~Bridge ID: " + str(self.bridge_ID) +
              " Root ID: " + str(self.config_BPDU[0]) + "~~~~~~")
        print("BPDU:")
        print(self.config_BPDU)

        print("MAC address | Port Type | Segment Number")
        for port in self.port_list:
            port.print_port()
