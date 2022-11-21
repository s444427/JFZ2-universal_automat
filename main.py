# Zadanie 2, laboratoria 2
# Do 7.11

def map_maker(filename):
    # 1. Read file
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    # print("-----LIST-----\n", lines, "\n--------------")

    # 2. Get the number of states

    # 3. Parse file to two parts: adjacencies and final states
    adj = []
    final_states = []

    for line in lines:
        # line = i.split(" ")
        if len(line.split(" ")) == 3:
            adj.append(line)
        else:
            final_states.append(int(line[0]))

    # print("ADJ: ", adj)
    # print("FIN_STAT: ", final_states)

    # 5. Fill the adjacency table
    count = 0
    map_size = 0
    for i in adj:
        count += 1
        x, y, value = i.split(" ")
        x, y = int(x), int(y)
        if x > map_size:
            map_size = x
        if y > map_size:
            map_size = y

    map_size += 1

    # 4. Prepare adjacency table (or map for short) of the graph
    rows, cols = (map_size + 1, map_size + 1)
    map = [['' for i in range(cols)] for j in range(rows)]
    for i in adj:
        x, y, value = i.split(" ")
        x, y = int(x), int(y)
        map[x][y] += value

    print("-----ADJACANCY TABLE-----\n", "\n---------------")
    for x in map:
        print(x)

    return map, map_size, final_states


if __name__ == '__main__':
    map, map_size, final_states = map_maker("automat.txt")
    # print(map)

    curr_state = [0]
    next_state = []

    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    for test_str in lines:
        curr_state = [0]
        next_state = []
        print('sample: ', test_str)
        # 1. Char by char
        for curr_char in test_str:
            # 2. State by state
            for k in curr_state:
                # 3. Go through all adjacencies of current nodes
                for j in range(0, map_size):
                    if curr_char in map[k][j]:
                        next_state.append(j)
                        print(curr_state, next_state, curr_char)
            curr_state = next_state
            next_state = []

        # Final decision
        decision = False
        for i in curr_state:
            # print(i)
            if i in final_states:
                decision = True

        # Submit decision
        f = open("output.txt", "a")

        if decision:
            f.write("tak\n")
        else:
            f.write("nie\n")
    f.close()
