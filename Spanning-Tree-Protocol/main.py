from simulator import simulator


def main():
    bridges = [
        [
            100,   # bridge_ID
            [         # list of ports
                [0, 0],  # each port is mac_address, segment_number
                [1, 1]
            ]
        ],
        [
            200,
            [
                [2, 1],
                [3, 2]
            ]
        ],
        [
            300,
            [
                [4, 2],
                [5, 3]
            ]
        ],
    ]

    # Scenario
    end_time = 800
    simulator(bridges, end_time)


if __name__ == '__main__':
    main()
