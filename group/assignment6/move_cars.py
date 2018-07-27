def generate_moves(start, final):
    """ ith element of start start is the car currently in the ith space
    ith element of final start is the car that should be in ith space
    empty space is 0
    yields optimal sequence of moves in format (car number, old space, new space) """

    # validation of the input
    start_set = set(start)
    final_set = set(final)
    #print(start_set, final_set)
    if len(start_set) != len(start) or start_set != final_set or \
       len(final_set) != len(final) or \
       start_set != final_set and 0 not in start_set:
        yield None

    # pos will contain car positions in another form
    pos = [0] * len(start)
    if 0 in start_set:
        for place, car in enumerate(start):
            pos[car] = place

        # main loop
        for car, place in enumerate(pos):
            if final[place] == car:
                continue

            if car:  # this is a cycle fix
                yield car, place, pos[0]
                pos[0], pos[car] = pos[car], pos[0]

            car = final[pos[0]]
            while car:
                yield car, pos[car], pos[0]
                pos[0], pos[car] = pos[car], pos[0]
                car = final[pos[0]]

def fancy_output(start, final):
    result = generate_moves(start, final)
    for i in result:
        if i:
            print("Move car number {} from {} to {}".format(*i))
        else:
            print("Unsolvable")
            break
    print("Done")

def return_output(start, final):
    result = generate_moves(start, final)
    output = []
    for i in result:
        if i:
            output.append("Move car number {} from {} to {}".format(*i))
        else:
            output = ["Unsolvable"]
            break
    return output

if __name__ == "__main__":
    fancy_output([1, 0, 2, 3, 4], [2, 3, 1, 4, 0])
