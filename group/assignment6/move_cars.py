def car_positions(state):
    """ given state returns array where ith element is the position of ith car """
    positions = [0] * len(state)
    for place, car in enumerate(state):
        positions[car] = place
    return positions


def generate_moves(start, final):
    """ ith element of start state is the car currently in the ith space
    ith element of final state is the car that should be in ith space
    empty space is 0
    yields optimal sequence of moves in format (car number, old space, new space) """

    pos = car_positions(start)
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
    for i in generate_moves(start, final):
        print("Move car number {} from {} to {}".format(*i))
    print("Done")


fancy_output([1, 0, 2, 3, 4], [2, 3, 1, 4, 0])
# fancy_output([1, 0, 2, 3, 4], [2, 0, 1, 4, 3])
