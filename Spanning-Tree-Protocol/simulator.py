from topology_reader import bridge_initializer


def simulator(bridges, end_time):
    # Initializing bridges
    bridges_dict = {}
    bridges_dict = bridge_initializer(bridges)  # bridge ID : bridge

    print("before STP")
    for b in bridges_dict:
        bridges_dict[b].print_bridge()

    # Calling bridges in round robin fashion
    for t in range(end_time):
        for b in bridges_dict:
            bridges_dict = bridges_dict[b].send_BPDUs(bridges_dict)
        for b in bridges_dict:
            bridges_dict = bridges_dict[b].receive_BPDUs(bridges_dict)

    print("after STP")
    for b in bridges_dict:
        bridges_dict[b].print_bridge()
