class single_linked_node:
    def __init__(self, value=None, child=None):
        self.child = child
        self.value = value

def return_k_th_from_end_element(k, start_node):
    list_len = 0
    current_node = start_node
    while (current_node):
        list_len += 1
        current_node = current_node.child
    element_num = list_len - k
    if element_num < 0 or element_num > list_len:
        print("wrong k")
        return None
    else:
        current_num  = 0
        current_node = start_node
        while(current_node):
            current_num += 1
            if current_num == element_num:
                return current_node.value
            current_node = current_node.child

if __name__ == "__main__":
    # Demonstration of the functional
    test_list = [single_linked_node(0, None)]
    for i in range(1, 10):
        test_list.append(single_linked_node(i, test_list[-1]))
    print("we generated list 0 <- 1 <- 2 <- 3 <- 4 <- 5 <- 6 <- 7 <- 8 <- 9 for example")

    current_node = test_list[-1] 
    while (current_node):
        current_node = current_node.child

    print("choose k for testing return_k_th_from_end_element function")
    k = int(input())
    print(return_k_th_from_end_element(k, test_list[-1]))
