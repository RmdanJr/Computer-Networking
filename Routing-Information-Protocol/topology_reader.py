from router import router_base
from router import router
from port import port_link
from port import port
from rip_packet import RIP_entry


def topology_to_routers(topology):
    router_list = []
    for rtr in topology:
        r = router(rtr[0], [], [])
        for prt in rtr[1:]:
            new_link = port_link(prt[1], prt[2], prt[3])
            new_port = port(prt[0], new_link)
            r.add_port(new_port)
        r.add_RIP_entry(None, rtr[0], 0, None)
        router_list.append(r)
    return(router_list)
