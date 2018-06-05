class single_linked_node:

    def __init__(self, value=None, child=None):
        self.child = child
        self.value = value

    def __getitem__(self, k):
        current_pos = 0
        k_th_back_node = self
        current_node = self
        while (current_node):
            if current_pos > -k:
                k_th_back_node = k_th_back_node.child
            current_node = current_node.child
            current_pos += 1
        list_len = current_pos
        if not k_th_back_node or -k >= list_len:
            raise IndexError("Index '%s' is out of range, due the length of the list is '%s'"\
                             % (-k, list_len))
        return k_th_back_node.value

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
