from ports import ports
from bridge import bridge


def bridge_initializer(bridges):
    bridges_dict = {}
    for brg in bridges:
        ports_list = [ports(port[0], port[1]) for port in brg[1]]
        bridges_dict[brg[0]] = bridge(brg[0], ports_list)
    for b in bridges_dict:
        bridges_dict[b].initialize_recv_queue(bridges_dict)
    return bridges_dict
