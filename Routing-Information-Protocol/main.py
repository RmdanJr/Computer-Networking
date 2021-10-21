from router import router
from rip_packet import RIP_entry
from rip_packet import RIP_packet
from port import port
from port import port_link
from topology_reader import topology_to_routers


def main():
    topology2 = [
        [1, [11, 2, 21, 1], [12, 4, 41, 1]],  # Routers and links
        # [IP of router, [link of router, IP of destination router, IP of link of destination router, cost]]
        [2, [21, 1, 11, 1], [22, 5, 53, 1], [23, 3, 31, 1]],
        [3, [31, 2, 23, 1], [32, 5, 52, 1]],
        [4, [41, 1, 12, 1], [42, 5, 51, 1]],
        [5, [51, 4, 42, 1], [52, 3, 32, 1], [53, 2, 22, 1]]
    ]
    topology = [
        [1, [11, 2, 21, 1], [12, 4, 41, 5]],  # Routers and links
        # [IP of router, [link of router, IP of destination router, IP of link of destination router, cost]]
        [2, [21, 1, 11, 1], [22, 5, 53, 1], [23, 3, 31, 4]],
        [3, [31, 2, 23, 4], [32, 5, 52, 1]],
        [4, [41, 1, 12, 5], [42, 5, 51, 1]],
        [5, [51, 4, 42, 1], [52, 3, 32, 1], [53, 2, 22, 1]]
    ]
    steps_to_run = 5
    router_list = topology_to_routers(topology)
    print("---------routers initialized---------")
    for r in router_list:
        r.print_router()

    # Simulator
    for i in range(steps_to_run):
        for j in range(len(router_list)):
            router_list = router_list[j].send_RIP_packets(router_list)
    print("---------routers after " + str(i) + " iterations---------")
    for r in router_list:
        r.print_router()


if __name__ == '__main__':
    main()
