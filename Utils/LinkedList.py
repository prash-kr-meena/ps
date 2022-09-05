from Utils.Array import input_array


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def input_linked_list() -> Node:
    """
    In our case, we do not need -1 to stop taking input
    """
    linked_list_data = input_array()

    temporary_node = Node(-9999999)
    head = tail = temporary_node  # To get rid off null check on head, in the loop

    # tail : will work as the moving_pointer
    for data in linked_list_data:
        new_node = Node(data)
        tail.next = new_node
        tail = tail.next

    return head.next  # passing over the temporary_node


def input_linked_list_with_end_value(end_of_linked_list=-1) -> Node:
    """
    Here to end the linked list input, end_of_linked_list value is required
    By default the end_of_linked_list value is -1
    """
    linked_list_data = input_array("LL :")

    temporary_node = Node(-9999999)
    head = tail = temporary_node  # To get rid off null check on head, in the loop

    # tail : will work as the moving_pointer
    for data in linked_list_data:
        if data == end_of_linked_list:
            break
        new_node = Node(data)
        tail.next = new_node
        tail = tail.next

    return head.next  # passing over the temporary_node


def print_linked_list(head) -> None:
    linked_list_data___in_str_format = []
    while head is not None:
        linked_list_data___in_str_format.append(str(head.data))
        head = head.next

    print(" -> ".join(linked_list_data___in_str_format))


def get_linked_list_size(head) -> int:
    length = 0
    while head is not None:
        length += 1
        head = head.next

    return length


if __name__ == "__main__":
    head_pointer = input_linked_list()
    print_linked_list(head_pointer)
    linked_list_length = get_linked_list_size(head_pointer)
    print(linked_list_length)

"""
3 4 5 2 6 1 9
10 76 39 -3 2 9 -23 9
"""
