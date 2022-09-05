# ------------------------------  Input Array   ------------------------------

def input_array(prompt="", sep=None) -> list:
    """
    input a list of space-separated integers <array>

    :param prompt:  The text prompt you want to show, for the user to enter data
    :param sep: The separator/delimiter to split the string on.
    Default is None, meaning split on white space. But can be split on ","  "." or any other String.
    :return: return a list of separated integers
    """
    return list(map(int, input(prompt).strip().split(sep)))


# ------------------------------  Printing Array   ------------------------------


def print_array_inline(arr: list) -> None:
    """
    # If you don't want space at the end of it
    :param arr: Array of elements (any)
    :return: None
    """
    list_of_string = list(map(str, arr))
    print(" ".join(list_of_string))


def print_array_by_traversing(arr: list) -> None:
    """
    If you want space at the end of it
    :param arr: Array of elements (any)
    :return: None
    """
    for element in arr:
        print(element, end=" ")
    print()


def print_array_multiline(arr: list) -> None:
    """
    If you want to print each element in seprate line
    :param arr: Array of elements (any)
    :return: None
    """
    for element in arr:
        print(element)


# ------------------------------  Reverse Array   ------------------------------

def reverse_array_inplace(arr: list, i: int, j: int):
    # Reverse Array Inplace b/w i to j, Both Inclusive
    n = len(arr)

    if i < 0 or i > n - 1 or j < 0 or j > n - 1:
        return Exception("Out of index")

    if j < i:
        return Exception("j > i Not allowed")

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


# ------------------------------  Swap Array Elements   ------------------------------
def swap_array_elements(arr: list, i: int, j: int) -> None:
    """
    Swap elements of an Array, ie swap arr[i] with arr[j]

    :param arr: Array of elements (any)
    :param i:   index i
    :param j:   index j
    :return:    None
    """
    arr[i], arr[j] = arr[j], arr[i]


# ------------------------------  Start Up   ------------------------------

if __name__ == "__main__":
    print(input_array("Input ',' separated integer values : ", sep=","))
    print(input_array("Input '*' separated integer values : ", sep="*"))
    print("\n")

    array = [1, 2, 3, 4]
    print_array_inline(array)
    print_array_by_traversing(array)
    reverse_array_inplace(array, 0, len(array) - 1)
    print("After reverse : ", array)
