from typing import List


def check_input(start: List[int], final: List[int]) -> bool:
    """ Method to check correctness of input
    Args:
        start: list of integers where ith element is the car currently in the
               ith space
        final: list of integers where ith element is the car that should be in
               the ith space
    Returns:
        bool: is the input correct
    """
    start_set = set(start)
    final_set = set(final)
    car_set = set([i for i in range(len(start))])

    # let's return False in the case of an empty sets
    if len(start_set) == 0 or len(final_set) == 0:
        return False

    if len(start) != len(car_set) or len(final) != len(car_set):
        return False

    # elements of both the start and final sets should be 0 to len(start) - 1
    return start_set == car_set and final_set == car_set


def _invert(state: List[int]) -> List[int]:
    """ Method to get the inverse of a list, i.e. value becomes the position
    and position becomes the value.
    Args:
        state: a list of integers from 0 to len(state) - 1 e.g [1, 2, 0, 3]
    Returns:
        List(int): inverse of the list e.g [2, 0, 1, 3]
    """
    new_state = [0] * len(state)
    for i, j in enumerate(state):
        new_state[j] = i
    return new_state


def _move(car_positions: List[int], car_num: int) -> int:
    """ Method to move car to current empty position
    Args:
        car_positions: list of integers where ith element is the current 
                       position of ith car
        car_num: int number of car to move
    Returns:
        int: new empty position
    """
    car_positions[0], car_positions[car_num] = \
    car_positions[car_num], car_positions[0]
    return car_positions[0]


def generate_moves(start: List[int], final: List[int]) -> List[int]:
    """ Method to yield optimal sequence of moves in format
    (car number, old space, new space)
    Args:
        start: list of integers where ith element is the car currently in the
               ith space
        final: list of integers where ith element is the car that should be in
               the ith space
    Returns:
        List[int]: returns final list of positions
                   (this should be equal to final and is only for testing)
    """

    # inverted list of start list,i.e.ith element is current position of ith car
    car_positions = _invert(start)
    empty_place = car_positions[0]
    for car, place in enumerate(car_positions):
        # if car is already where it is supposed to be, do nothing
        if car == final[place]:
            continue

        # if car exists, break the cycle by moving car to empty position
        if car:
            yield car, place, empty_place
            empty_place = _move(car_positions, car)

        # move car that should end up in current empty space while such a car
        # exists
        while final[empty_place]:
            current_car = final[empty_place]
            yield current_car, car_positions[current_car], empty_place
            empty_place = _move(car_positions, current_car)

    return _invert(car_positions)


def fancy_output(start, final):
    for i in generate_moves(start, final):
        print("Move car number {} from {} to {}".format(*i))
    print("Done")

if __name__ == "__main__":
    fancy_output([1, 0, 2, 3, 4], [2, 3, 1, 4, 0])
    fancy_output([1, 0, 2, 3, 4], [2, 0, 1, 4, 3])
