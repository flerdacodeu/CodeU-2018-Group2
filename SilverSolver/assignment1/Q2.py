from collections import deque

class single_linked_node:

    def __init__(self, value=None, child=None):
        self.child = child
        self.value = value

    def __getitem__(self, k, one_pass=True):
        list_len = 0
        visited_nodes = deque(maxlen=-k + 1)
        current_node = self
        while (current_node):
            # if we want optimize by time and do one_pass through the
            # linked list, we should keep k last visited nodes
            if one_pass:
                visited_nodes.append(current_node)                
            list_len += 1
            current_node = current_node.child
        element_num = list_len + k
        if element_num > list_len or element_num <= 0:
            raise IndexError("Index '%s' is out of range, due the length of the list is '%s'"\
                             % (-k, list_len))
        else:
            if one_pass:
                return visited_nodes.popleft().value
            else:
                # if we didn't keep k last visited nodes, we will go
                # through the linked list again
                current_num  = 0
                current_node = self
                while(current_node):
                    current_num += 1
                    if current_num == element_num:
                        return current_node.value
                    current_node = current_node.child


def from_iterable(iterable):
    prev_node = single_linked_node(iterable[0], None)
    for i in range(1, len(iterable)):
        prev_node = single_linked_node(iterable[i], prev_node)
    return prev_node

def return_k_th_from_end_element(k, node):
    return node[-k]


if __name__ == "__main__":
    # Demonstration of the functional

    iterable = [i for i in range(10)]
    example_list = from_iterable(iterable) 
    print("we generated list 0 <- 1 <- 2 <- 3 <- 4 <- 5 <- 6 <- 7 <- 8 <- 9 for example")
    print("choose k for testing return_k_th_from_end_element function")
    k = int(input())
    print(return_k_th_from_end_element(k, example_list))
