class ports():
    def __init__(self, mac_address, segment_number, port_type=1):
        self.mac_address = mac_address  # Numberic mac address
        self.port_type = port_type     # Blocking = 0, Forwarding = 1, root = 2
        self.segment_number = segment_number

    def get_reachable_bridge_ID(self, bridges_dict, calling_bridge_id):
        bridge_id_list = []
        for b in bridges_dict:
            for p in bridges_dict[b].port_list:
                if p.segment_number == self.segment_number and bridges_dict[b].bridge_ID != calling_bridge_id:
                    bridge_id_list.append(b)
        return bridge_id_list

    def get_port_state(self):
        return self.port_type

    def print_port(self):
        print(str(self.mac_address) + " | ", end=" ")
        if self.port_type == 0:
            print("Blocking | ", end=" ")
        elif self.port_type == 1:
            print("Forwarding | ", end=" ")
        elif self.port_type == 2:
            print("Root | ", end=" ")
        print(str(self.segment_number))
