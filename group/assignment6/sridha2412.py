from typing import List

def _get_inverse(state: List[int]) -> List[int]:
    """ Method to get the inverse of a list i.e value becomes the position and position becomes the value
    Args:
        state: a list of integers e.g [1, 2, 0, 3]
    Returns:
        List(int): inverse of the list e.g [2, 0, 1, 3]
    """
    new_state = [0] * len(state)
    for i, j in enumerate(state):
        new_state[j] = i

    return new_state


def _swap(state: List[int], state_inv: List[int], move_to: int, move_from: int) -> List[int]:
    """ Method to swap elements of given list and its inverse list at given positions
    Args:
        state: list of integers
        state_inv: inverse of given state
        move_to: int position to swap element
        move_from: int position to swap element

    Returns:
        List[int]: new list with swapped elements of state
        List[int]: new list with swapped element of inverse state
    """

    state[move_to], state[move_from] = state[move_from], state[move_to]
    state_inv[state[move_to]], state_inv[state[move_from]] = state_inv[state[move_from]], state_inv[state[move_to]]

    return state, state_inv

def generate_moves(start: List[int], final: List[int]) -> List[int]:
    """ Method to yield optimal sequence of moves in format (car number, old space, new space)
    Args:
        start: list of integers where ith element is the car currently in the ith space
        final: list of integers where ith element is the car that should be in the ith space
    Returns:
        List[int]: returns final list of position (this should be equal to final and is only for testing)
    """

    # inverted lists of both lists
    start_inv = _get_inverse(start)
    final_inv = _get_inverse(final)

    for car, place in enumerate(start_inv):

        # if empty space or car is already where it is supposed to be
        if car == 0 or car == final[place]:
            continue

        else:
            # find actual place of car
            actual_place = final_inv[car]
            # find empty place
            empty_place = start_inv[0]

            # swap
            # move car from actual place to empty place
            if(actual_place != empty_place):
                yield start[actual_place], actual_place, empty_place
                start, start_inv = _swap(start, start_inv, actual_place, empty_place)

             # move current car to the now empty actual place
            yield car, place, actual_place
            start, start_inv = _swap(start, start_inv, actual_place, place)

    # print(start)
    return start


def fancy_output(start, final):
    for i in generate_moves(start, final):
        print("Move car number {} from {} to {}".format(*i))
    print("Done")

# fancy_output([1, 0, 2, 3, 4], [2, 3, 1, 4, 0])
# fancy_output([1, 0, 2, 3, 4], [2, 0, 1, 4, 3])
