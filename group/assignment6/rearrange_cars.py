import unittest

def inverse_map(state):
    """ Returns array indexed with previous values. """
    inversed = len(state) * [0]

    for position, car in enumerate(state):
        inversed[car] = position

    return inversed

def move_car(start, start_position, current_empty):
    """
        Moves car from start_position to empty place.
        Returns new empty place and configuration with moved car.
    """
    start[start_position], start[current_empty], current_empty = start[current_empty], start[start_position], start_position
    return (current_empty, start)

def find_sequence(start, end):
    """
        Yields sequence of moves between start and end states.
    """
    current_empty = start.index(0)
    end_positions = inverse_map(end)
    
    for position in range(len(start)):
        # At first, move car, that should be placed in current
        # empty space and repeat.
        while end_positions[0] != current_empty:
            start_positions = inverse_map(start)
            current_empty, start = move_car(start, start_positions[end[current_empty]], current_empty)
            yield start
            
        car = start[position]
        
        if end[position] != car and car != 0:
            end_position = end_positions[car]

            # Move car from end position to empty place
            if end_position != current_empty:
                current_empty, start = move_car(start, end_position, current_empty)
                yield start

            # Move current car to end position
            current_empty, start = move_car(start, position, current_empty)
            yield start
            
def print_sequence(start, end):
    print(start)
    for i in find_sequence(start, end):
        print(i)
    print("\n")

class TestCarSequences(unittest.TestCase):
    def test(self):
        print_sequence([1, 2, 0, 3], [3, 1, 2, 0])
        print_sequence([0, 1, 2, 3], [0, 3, 2, 1])
        print_sequence([1, 2, 3, 4, 0], [2, 1, 0, 4, 3])
        print_sequence([1, 2, 3, 0], [0, 1, 2, 3])
        print_sequence([5, 2, 1, 0, 4, 3], [3, 4, 0, 5, 1, 2])

if __name__ == '__main__':
    unittest.main()
